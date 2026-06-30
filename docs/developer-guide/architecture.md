# Theme Architecture

## Folder structure

```
theme/
├── assets/          # CSS, JS, images, fonts
├── config/          # settings_schema.json, settings_data.json
├── layout/          # theme.liquid and any alternate layouts
├── locales/         # translation files
├── sections/        # reusable, schema-driven page sections
├── snippets/         # render-only partials, no schema
├── templates/        # JSON templates mapping sections to pages
└── blocks/           # (OS 2.0) reusable blocks within sections
```

## Conventions used in this theme

- **`{% render %}` over `{% include %}`** — `render` is scoped (no variable leakage
  between snippet and parent), which is why it's the default here. `include` is only
  used where intentional scope-sharing is needed — flag any new `include` usage in
  review.
- **Section schema** — *(document your naming/setting conventions here once decided)*
- **`theme.liquid`** — kept minimal; logic that doesn't need to run on every page
  should not live here.

## Metafields & Metaobjects

This theme uses Shopify **metaobjects** as a managed, reusable value pool for
attributes like fit, material, and color — referenced from product metafields
rather than hardcoded as plain text. This lets merchants add new values from
Shopify admin without a developer touching schema.

Key things to know:

- Metaobject-referenced metafields require the **double `.value`** dereference in
  Liquid (`product.metafields.custom.fit.value.value` style access, depending on
  field type) — easy to miss.
- **Storefront access** must be explicitly enabled per metafield definition in
  Shopify admin, or the reference will not resolve on the storefront even though it
  shows correctly in admin.
- Namespace/key paths shown in code examples (e.g. `custom.fit_type`) are
  placeholders — always confirm the actual namespace/key in
  **Settings → Custom data** before copying a snippet.

## Performance notes

*(Document image handling, lazy-loading conventions, section rendering API usage,
JS bundling approach, etc. as they're finalized.)*
