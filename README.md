# Ang-Kun Wu — personal website

Static personal website for **https://angkunwu.github.io/**. Content updated November 20, 2026.

The site includes research interests, 17 journal articles and 6 preprints, eight software projects, research experience, education, honors, technical skills, applied projects, talks, teaching, and peer-review service. The full publication list is available without JavaScript. Search and filters appear when JavaScript is enabled. Fonts, styles, scripts, illustration, and bibliography are local assets.

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
- To refresh publications, update the public copy at `assets/publications.bib`. Keep source-code links and published distinctions in the addenda. Then run the generator.

```sh
python3 scripts/update_publications.py
```

The Python script rewrites the publication block and keeps papers in descending year order, preserving bibliography order within each year. Published papers use `article`, and preprints use `misc` with an arXiv identifier. The renderer displays `misc` entries without an arXiv identifier as manuscripts in preparation and includes any supplied source-code links. Filters appear for categories with entries.

- Update the publication count and revision date in `index.html` and this README. Set the sitemap's `lastmod` to the publication date when deploying.

Use **Ang-Kun Wu** as the public display name, matching the publication name. The GitHub username, site URL, email address, and linked profile URLs retain their existing spelling. The AW favicon uses the initials of the given name and surname.

Introduce the author as a **theoretical and computational physicist**. Use direct descriptions of research and straightforward section headings; omit decorative numbering, portfolio slogans, and illustration captions. Keep the lattice as an abstract illustration. Employment titles belong in the Experience section. Keep the website self-contained: include experience and accomplishments in the page rather than publishing CV PDFs or download links.
