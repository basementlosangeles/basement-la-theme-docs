# FAQ Page

`sections/faq-page.liquid`

## What it does

The FAQ page — a title plus a list of expandable question/answer rows. The Q&A rows
are `faq-dropdown-item` theme blocks; the section only owns the heading.

## Where it's used

Assigned in `templates/page.FAQ.json`, using the `page-text-theme` layout. The
template wires several `faq-dropdown-item` blocks (and an `ai_gen_block_*`). Preset
name: **FAQ Page**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `title-text` | Title Text | text | `FAQ` |

Content blocks accepted: `"blocks": [{ "type": "@theme" }]`.

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- Adding or editing questions is a block operation (`faq-dropdown-item`), not a
  settings change — the only section setting is the page title.
