# Announcement Bar

`sections/announcement-bar.liquid`

## What it does

The thin promo strip at the very top of the site (e.g. "FREE SHIPPING ON US ORDERS
175+"). Supports an optional countdown timer that counts down to a configured
drop date/time, with its own color treatment.

## Where it's used

Lives in **both** header section groups — `sections/header-group.json` and
`sections/header-group-no-background.json` — so it appears on every page whose
layout pulls in a header group (i.e. everything except the password page). Preset
category: **Header Group**.

Because it's part of a section group, its saved values differ per group (the two
groups ship different announcement copy and drop dates).

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `announcement_text` | Announcement Text | text | `FREE SHIPPING ON US ORDERS 175+` |
| `announcement_text_color` | Announcement Text Color | color | `#ffffff` |
| `announcement_background_color` | Announcement Background Color | color | `#3b3b3bff` |
| `is-countdown-enabled` | Is Countdown Enabled? | checkbox | `false` |
| `date-time-before-drop` | Date and Time Before Drop | text | `08/25/2025 15:50:00` |
| `time_text_color` | Time Block Text Color | color | `#3A3A3A` |
| `time_background_color` | Time Block Background Color | color | `#d9d9d9ff` |

`date-time-before-drop` is a free-text field parsed as `mm/dd/yyyy hh:mm:ss` — there
is no date picker, so the format must be exact or the countdown JS will fail.

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- The countdown is driven by inline JS reading `date-time-before-drop`; mistyped
  dates are a common cause of a stuck or blank timer.
- Height is part of the layout math — the announcement bar height feeds
  `--sm--announcement-bar-height` in `snippets/css-variables.liquid`. Changing the
  bar's size means updating that token, not just this section.
