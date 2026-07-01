# Policy Page Section

`sections/policy-page-section.liquid`

## What it does

A content container for long-form legal/policy pages (e.g. Privacy Policy). It holds
no settings of its own; the page is assembled from `policy-page-*` theme blocks —
headers, text, nested bullet lists, and tables.

## Where it's used

Assigned (multiple times) in `templates/page.Privacy-Policy.json`, using the
`page-text-theme` layout. Preset category: **Main**.

## Schema settings

None (`"settings": []`). Content blocks accepted: `"blocks": [{ "type": "@theme" }]`.
Blocks used by the Privacy Policy template:

- `policy-page-header` — section heading
- `policy-page-text` — paragraph text
- `policy-page-bullet-parent` / `policy-page-bullet-item` — nested bullet lists
- `policy-page-table` / `policy-page-table-row` / `policy-page-table-header` /
  `policy-page-table-data` — tabular content

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- This is the **active** policy section. The older [`policy-page`](policy-page.md)
  section is not referenced by any template and appears superseded.
- Editing policy content is entirely a block operation — no merchant-guide page is
  provided since there are no section settings to document.
