#!/usr/bin/env python3
"""Render the checked-in CV bibliography into index.html; no dependencies required."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]

def tex_text(value):
    value = re.sub(r"\{\\'e\}", 'é', value)
    value = re.sub(r'\{\\c\{c\}\}', 'ç', value)
    value = value.replace('\\&', '&').replace('~', ' ')
    value = re.sub(r'\\[a-zA-Z]+\s*', '', value)
    return ' '.join(value.replace('{', '').replace('}', '').split())

def parse_bib(source):
    # Balanced braces preserve nested TeX accents and protected capital letters.
    for match in re.finditer(r'@(article|misc)\s*\{\s*([^,]+),', source):
        pos = match.end()
        fields = {}
        while pos < len(source):
            field = re.match(r'\s*,?\s*([\w+]+)\s*=\s*\{', source[pos:])
            if not field:
                break
            key = field.group(1)
            start = pos + field.end()
            depth, end = 1, start
            while depth and end < len(source):
                if source[end] == '{': depth += 1
                elif source[end] == '}': depth -= 1
                end += 1
            if depth:
                raise ValueError(f'Unbalanced field in {match.group(2)}')
            fields[key] = source[start:end - 1]
            pos = end
        for required in ('author', 'title', 'year'):
            if required not in fields:
                raise ValueError(f'Missing {required} in {match.group(2)}')
        yield match.group(1), fields

def render(kind, fields):
    escape = html.escape
    title = tex_text(fields['title'])
    authors = []
    for author in fields['author'].split(' and '):
        name = tex_text(author)
        if ',' in name:
            last, first = name.split(',', 1)
            name = first.strip() + ' ' + last.strip()
        escaped = escape(name)
        if re.fullmatch(r'(A\.-K\.|Ang-Kun) Wu', name):
            escaped = '<strong>' + escaped + '</strong>'
        authors.append(escaped)
    year = tex_text(fields['year'])
    url = fields.get('url') or ('https://doi.org/' + fields['doi'] if fields.get('doi') else 'https://arxiv.org/abs/' + fields['eprint'])
    if kind == 'article':
        venue = tex_text(fields['journal'])
        if fields.get('volume'): venue += ' ' + tex_text(fields['volume'])
        if fields.get('pages'): venue += ', ' + tex_text(fields['pages'])
        venue += ' (' + year + ')'
    else:
        venue = 'arXiv:' + fields['eprint'] + ' · Preprint (' + year + ')'
    note = fields.get('addendum', '')
    code = re.search(r'\\url\{([^}]+)\}', note)
    if code:
        note_html = f'<p class="paper-note"><a href="{escape(code.group(1), quote=True)}">Source code ↗</a></p>'
    elif note:
        note_html = f'<p class="paper-note">{escape(tex_text(note))}</p>'
    else:
        note_html = ''
    return f'''    <li class="publication" data-type="{kind}"><span class="publication-year">{escape(year)}</span><div><h3><a href="{escape(url, quote=True)}">{escape(title)}</a></h3><p>{', '.join(authors)}</p><p class="venue">{escape(venue)}</p>{note_html}</div></li>'''

def main():
    entries = list(parse_bib((ROOT / 'assets/publications.bib').read_text()))
    entries.sort(key=lambda item: int(item[1]['year']), reverse=True)
    if not entries:
        raise ValueError('No bibliography entries found')
    target = ROOT / 'index.html'
    page = target.read_text()
    start, end = '<!-- PUBLICATIONS:START -->', '<!-- PUBLICATIONS:END -->'
    if page.count(start) != 1 or page.count(end) != 1:
        raise ValueError('Publication markers must appear exactly once')
    prefix, rest = page.split(start)
    _, suffix = rest.split(end)
    target.write_text(prefix + start + '\n' + '\n'.join(render(*entry) for entry in entries) + '\n' + end + suffix)
    print(f'Rendered {len(entries)} publications.')

if __name__ == '__main__':
    main()
