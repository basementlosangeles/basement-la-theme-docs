# Password

`sections/password.liquid`

## What it does

The storefront password page shown when the store is locked (e.g. before a drop). It
has a title, a countdown to the drop time, a scrolling image carousel (built from
`password-item` blocks), a password input, and a Klaviyo subscribe form.

## Where it's used

Assigned in `templates/password.json`, using the `password-theme` layout — the only
layout with **no header group, cart, radio, code-popup, or footer**. Preset name:
**Password**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `show-password-page` | Show Password Page | checkbox | `false` |
| `klaviyo-form-id` | Klaviyo Form ID | text | — |
| `title-text` | Title Text | text | `New Drop` |
| `date-time-before-drop` | Date and Time Before Drop | text | `08/25/2025 15:50:00` |
| `countdown-done-text` | Countdown Done Text | text | `Please Wait A Moment` |
| `is-scrolling-img-carousel` | Scroll Image Carousel? | checkbox | `true` |
| `img-carousel-scroll-speed` | Img Carousel Speed | number | `1` |
| `password-input-placeholder-text` | Password Input Placeholder | text | `Password` |
| `password-btn-text` | Password Button Text | text | `Password` |
| `enter-btn-text` | Enter Button Text | text | `Enter` |
| `subscribe-btn-text` | Subscribe Button Text | text | `Subscribe` |

Accepts `"blocks": [{ "type": "@theme" }, { "type": "@app" }]` — carousel images are
`password-item` blocks.

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- `show-password-page` is an **editor-preview toggle** ("[Leave Disabled in
  Production!]") — it lets you style the page in the customizer without actually
  locking the store. The real lock is Shopify's **Online Store → Preferences →
  Password** setting.
- `img-carousel-scroll-speed` must be an **integer** — the inline note warns Safari
  doesn't handle decimal speeds.
- `date-time-before-drop` is free text parsed as `mm/dd/yyyy hh:mm:ss`.
