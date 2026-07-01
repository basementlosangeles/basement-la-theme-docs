# Spacer

`sections/spacer.liquid`

## What it does

A utility section that inserts vertical whitespace. It can apply one uniform spacing
value, or separate mobile and desktop values via a toggle.

## Where it's used

Not placed in any template by default — it's a reusable preset ("Spacer") a merchant
can drop between sections in the editor.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `has-mobile-and-desktop-variants` | Has Mobile and Desktop Variants? | checkbox | `false` |
| `spacing` | Spacing (PX) | number | `0` |
| `mobile--spacing` | Mobile Spacing (PX) | number | `0` |
| `desktop--spacing` | Desktop Spacing (PX) | number | `0` |

`visible_if` gates the fields: `spacing` shows when the variants toggle is **off**;
`mobile--spacing` / `desktop--spacing` show when it's **on**.

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- Pure layout helper — no content, no data dependencies.
- Use the variants toggle when mobile and desktop need different gaps; otherwise the
  single `spacing` value applies everywhere.
