# Code Popup

`sections/code-popup.liquid`

## What it does

A multi-step discount-code capture modal (email → phone → code → claim). Each step
is a `code-popup-*-view` theme block. Visibility is CSS-driven via `.display-none`
on `#code-popup-container`; the popup appears after a configurable delay.

## Where it's used

Rendered **globally by layouts** — present in `theme`, `page-cover-theme`, and
`page-text-theme`. It is **commented out** in `homepage-theme` and **absent** from
`page-text-theme-no-code-popup` (the variant chosen specifically to suppress it, used
by Signup and restock-alert). Preset name: **Code Popup**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `is-enabled` | Is Enabled? | checkbox | `true` |
| `popup-appear-delay` | Popup Appear Delay (S) | number | `5` |
| `cancel-button-text` | Cancel Button Text | text | `I don't want my gift` |
| `cancel-button-text-color` | Cancel Button Text Color | color | `#060607` |
| `cancel-button-background-color` | Cancel Button Background Color | color | `#595344` |
| `cancel-button-border-color` | Cancel Button Border Color | color | `#060607` |

The popup's primary and text colors come from the global `Code Popup Settings`
theme settings (`code-popup-primary-color`, `code-popup-text-color`), not this
section.

## Metafields & metaobjects

None.

## Snippets rendered

None directly (the step views are blocks).

## Notes

- Two independent ways to turn it off: the `is-enabled` setting, and choosing a
  layout that doesn't render it (`page-text-theme-no-code-popup`). Both exist on
  purpose — the layout choice guarantees it never fires on conversion-sensitive pages.
- Steps live in `blocks/code-popup-email-view.liquid`, `…-phone-view`, `…-code-view`,
  `…-claim-view`.
