# Basement Radio Sidebar

`sections/radio-sidebar.liquid`

## What it does

A site-wide slide-out audio/radio panel. Tracks are `radio-sidebar-track` theme
blocks; the section controls the panel's color scheme, the mobile exit-arrow label,
and a fallback image used when a track's artwork fails to load.

## Where it's used

Rendered **globally by layouts** — `theme`, `homepage-theme`, `page-cover-theme`,
`page-text-theme`, and `page-text-theme-no-code-popup`. Preset name:
**Basement Radio Sidebar**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `mobile--exit-arrow-text` | Mobile Exit Arrow Text | text | `Click Arrow to Exit` |
| `primary-color` | Primary Color | color | `#3a3a3a` |
| `secondary-color` | Secondary Color | color | `#000000` |
| `background-color` | Background Color | color | `#d7d8d7` |
| `button-selected-color` | Button Selected Color | color | `#999999` |
| `radio-default-img` | Radio Default Image | image_picker | — |

Accepts `"blocks": [{ "type": "@theme" }]` for the track list.

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- Tracks (audio + artwork) are blocks, not settings — managing the playlist is a
  block operation.
- `radio-default-img` is the fallback shown only when a track image fails to load.
