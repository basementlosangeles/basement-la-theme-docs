# Homepage

`sections/homepage.liquid`

## What it does

A full-screen hero section supporting either a background **image** or **video**
(separate mobile/desktop sources), an overlay + gradient treatment, and a single
"Enter Basement" call-to-action button.

!!! warning "Currently unassigned"
    This section has a preset ("Homepage") but is **not assigned to any template**.
    `templates/index.json` builds the live homepage from the
    [`collection`](collection.md) section instead. Treat `homepage` as a
    legacy/alternate hero until confirmed with the team — verify before documenting
    it as the active homepage for merchants.

## Where it's used

Not referenced by any template or layout at time of writing. Preset name:
**Homepage**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `media-type` | Media Type | select (image/video) | `image` |
| `mobile--background-image` | Mobile Background Image | image_picker | — |
| `desktop--background-image` | Desktop Background Image | image_picker | — |
| `mobile--background-image-x-pos` | Mobile BG Image X Pos (%) | number | `0` |
| `mobile--background-image-y-pos` | Mobile BG Image Y Pos (%) | number | `0` |
| `mobile--background-image-zoom` | Mobile BG Image Zoom (%) | number | `100` |
| `desktop--background-image-x-pos` | Desktop BG Image X Pos (%) | number | `0` |
| `desktop--background-image-y-pos` | Desktop BG Image Y Pos (%) | number | `2` |
| `desktop--background-image-zoom` | Desktop BG Image Zoom (%) | number | `105` |
| `mobile--background-video` | Mobile Background Video | video | — |
| `desktop--background-video` | Desktop Background Video | video | — |
| `background-overlay-color` | Background Overlay Color | color (alpha) | `rgba(0,0,0,0.2)` |
| `background-graident-color` | Desktop Background Gradient Color | color | `#000000` |
| `desktop--background-graident-opacity` | Desktop Gradient Opacity (%) | range 0–100 | `30` |
| `desktop--background-graident-y-pos` | Desktop Gradient End Y Pos (%) | range 0–100 | `30` |
| `text-color` | Text Color | color | `#ffffff` |
| `text` | Text | text | `Enter Basement` |
| `btn-link` | Button Link | url | `/collections/all` |

Image/video fields are gated by `visible_if` on `media-type`.

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- "graident" is a misspelling baked into the setting ids (`background-graident-color`,
  `desktop--background-graident-*`) — match it exactly in Liquid; don't "fix" the id
  or saved values break.
- Uses Shopify-hosted `video` settings, so background video is uploaded through the
  asset picker rather than embedded.
