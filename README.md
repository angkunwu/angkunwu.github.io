# Ang-Kun Wu — personal website

Static personal website for **https://angkunwu.github.io/**. Content updated October 6, 2026.

The site includes research interests, all 22 bibliography entries, five open-source projects, full research experience, education, honors, technical skills, training, talks, teaching, and peer-review service. Publication searching and filtering are optional JavaScript enhancements; the full content is available without JavaScript. Fonts, styles, scripts, illustration, and bibliography are local assets.

## Preview locally

From this directory:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. No installation or build step is required.

## Publish with GitHub Pages

The repository remote is `https://github.com/angkunwu/angkunwu.github.io.git`.

1. Commit and push the website files to `main`.
2. In the repository, open **Settings → Pages**.
3. Select **Deploy from a branch**, then **main** and **/ (root)**, and save.
4. Visit https://angkunwu.github.io/ after deployment completes.

The `.nojekyll` file tells branch-based GitHub Pages publishing to skip Jekyll processing. This site uses plain HTML, CSS, and JavaScript; keeping the file makes that choice explicit. See [GitHub’s Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Update content

- Edit the biography, experience, research, software, teaching, and talks directly in `index.html`.
- Edit styling in `assets/css/style.css` and publication interactions in `assets/js/main.js`.
- To refresh publications, update `assets/publications.bib`, then run:

```sh
python3 scripts/update_publications.py
```

The Python script rewrites only the publication block, preserving the rest of the page. It keeps papers in descending year order while preserving bibliography order within a year. Publication status comes from the bibliography (`article` versus `misc`), including the “in press” note where supplied.

- Update the bibliography date note and footer when refreshing the content.

Use **Ang-Kun Wu** as the public display name, matching the publication name. The GitHub username, site URL, email address, and linked profile URLs retain their existing spelling. The AW favicon uses the initials of the given name and surname.

Introduce the author as a **theoretical and computational physicist**. Use direct descriptions of research and straightforward section headings; omit decorative numbering, portfolio slogans, and illustration captions. Keep the lattice as an abstract illustration. Employment titles belong in the Experience section. Keep the website self-contained: include experience and accomplishments in the page rather than publishing CV PDFs or download links.
