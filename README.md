# mkdocs-large-site

This is just a demo of a mkdocs static website capable of serving a gazillion of html static pages. Since the actual pages are not indexed by mkdocs, there is no slow down during the build phase and the navigation is lightweight. However, frontend search doesn't work, since no html page is indexed by mkdocs.

Inspired by: https://github.com/squidfunk/mkdocs-material/issues/1210

If this is useful to you but you prefer to stick with markdown documents rather than html, you might consider using pandoc to convert your markdown files to html.

## Running

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generate_index_pages.py
mkdocs build
mkdocs serve
```