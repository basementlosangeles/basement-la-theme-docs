# Signup

`sections/signup.liquid`

## What it does

A standalone email-capture / "new drop coming soon" landing section backed by a
Klaviyo form. Supports an optional hero image and an optional countdown to the drop.

## Where it's used

Assigned in **two** templates — `templates/page.Signup.json` and
`templates/page.restock-alert.json` — both using the
`page-text-theme-no-code-popup` layout (so the discount code-popup never fires on
these conversion pages). Preset name: **Signup**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `klaviyo-form-id` | Klaviyo Form ID | text | `X4vx3V` |
| `title-text` | Title Text | text | `NEW DROP COMING SOON` |
| `subtitle-text` | Subtitle Text | text | `SIGN UP TO BE THE FIRST TO KNOW` |
| `show-image` | Show Image | checkbox | `true` |
| `image` | Image | image_picker | — |
| `show-countdown` | Show Countdown | checkbox | `false` |
| `date-time-before-drop` | Date and Time Before Drop | text | `12/31/2025 15:00:00` |
| `countdown-done-text` | Countdown Done Text | text | `DROP IS LIVE` |

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- One section, two pages: the **Signup** page and the **Restock Alert** page both use
  it, so each template instance keeps its own form ID, copy, and image.
- The `-no-code-popup` layout is chosen deliberately here — don't switch these
  templates to a code-popup layout.
- `date-time-before-drop` is free text parsed as `mm/dd/yyyy hh:mm:ss`.
