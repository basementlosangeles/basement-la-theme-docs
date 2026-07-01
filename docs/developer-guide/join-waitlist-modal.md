# Join Waitlist Modal

`sections/join-waitlist-modal.liquid`

## What it does

A "Notify Me When Available" modal backed by a Klaviyo form. It adapts its layout
for product pages vs. other pages via a toggle, and exposes title, background, and
backdrop styling.

## Where it's used

Assigned in `templates/product.json`, `templates/index.json`, and
`templates/collection.json` (all `theme` layout). Preset category: **Pages**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `is-modal-for-product-page` | Is Modal for Product Page? | checkbox | `false` |
| `klaviyo-form-id` | Klaviyo Form ID | text | — |
| `title-text` | Modal Title Text | text | `Notify Me When Available` |
| `background-color` | Background Color | color | `rgba(170,170,170,1)` |
| `backdrop-color` | Backdrop Color | color (alpha) | `rgba(17,17,17,0.2)` |

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- `klaviyo-form-id` is the random-character ID from the Klaviyo form editor — the
  modal is inert until it's set.
- Because the same section is placed on product, index, and collection templates,
  each placement keeps its own settings — `is-modal-for-product-page` should be on
  only for the product-page instance.
