# Basement LA Theme Docs

Source for the Basement LA theme documentation site — merchant guide + developer docs,
built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), deployed to
GitHub Pages.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000 — it live-reloads as you edit files in `docs/`.

## Deploying

Push to `main`. The GitHub Action in `.github/workflows/deploy.yml` builds the site
and pushes it to the `gh-pages` branch automatically.

**One-time setup after creating the repo on GitHub:**

1. Update `site_url` and `repo_url` in `mkdocs.yml` to match your actual GitHub
   username/repo name.
2. Push this code to `main` on GitHub.
3. In the repo: **Settings → Pages → Source → Deploy from a branch → `gh-pages` / `root`.**
4. Your site will be live at `https://<username>.github.io/<repo-name>/` — no domain
   purchase needed.

## Adding content

- Merchant-facing pages go in `docs/merchant-guide/`
- Developer-facing pages go in `docs/developer-guide/`
- GIFs go in `docs/assets/gifs/` (keep them small — a few MB max)
- For longer screen recordings, upload as an **unlisted** YouTube/Loom video and
  embed via iframe rather than committing the file — see
  `docs/merchant-guide/example-feature.md` for the pattern.
- Register every new page in the `nav:` block of `mkdocs.yml`, or it won't show up
  in the sidebar even though the file exists.
