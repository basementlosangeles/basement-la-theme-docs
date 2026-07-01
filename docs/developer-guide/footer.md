# Footer

`sections/footer.liquid`

## What it does

The site footer — two menus (main + social), an optional "Early Access" email
capture, the Basement logo link, and copyright text, with full color control.

## Where it's used

Rendered **globally by layouts** (`page-cover-theme`, `page-text-theme`,
`page-text-theme-no-code-popup`, `theme`, and `theme.gempages.footer`) and also
referenced explicitly in `templates/password.json`. Preset category: **Layout**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `footer-main-menu` | Footer Main Menu | link_list | — |
| `footer-social-menu` | Footer Social Menu | link_list | — |
| `text-color` | Text Color | color | `rgba(255,255,255,1)` |
| `text-hover-color` | Text Hover Color | color | `rgba(170,170,170,1)` |
| `background-color` | Background Color | color | `rgba(17,17,17,1)` |
| `border-color` | Border Color | color (alpha) | `rgba(255,255,255,0.1)` |
| `is-early-access-enabled` | Enable Early Access? | checkbox | `true` |
| `label-text` | Early Access Label Text | text | `Get Early Access` |
| `placeholder-input-text` | Early Access Placeholder Input Text | text | `Email` |
| `basement-logo-link` | Basement Logo Link | url | `/` |
| `copyright-text` | Copyright Text | text | `@Basement 2025.` |

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- `footer-main-menu` and `footer-social-menu` are `link_list` settings — the actual
  links are managed under **Shopify Admin → Content → Menus** and selected here.
- `copyright-text` is plain text, so the year does not auto-update — it's a manual
  edit each year.
