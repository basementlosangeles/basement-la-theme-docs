# Default Page

`sections/default-page.liquid`

## What it does

The generic/fallback page section — what a plain Shopify page renders with when no
specialized template (About, FAQ, Contact, etc.) applies. It has no settings and no
blocks; it simply outputs the page's body content within the text layout.

## Where it's used

Assigned in `templates/page.json` (the default `page` template), using the
`page-text-theme` layout. Preset category: **Main**.

## Schema settings

None (`"settings": []`, `"blocks": []`).

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- Nothing here is merchant-editable in the theme editor — page copy is edited under
  **Shopify Admin → Content → Pages**, not the customizer. There is intentionally no
  merchant-guide page for this section.
