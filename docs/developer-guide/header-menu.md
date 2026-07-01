# Header Menu

`sections/header-menu.liquid`

## What it does

The main navigation bar and its associated drawers/sidebars. It composes a set of
theme blocks: `header-sidebar` (mobile menu), `header-sidebar-home-view`,
`header-sidebar-shop-view`, `header-shop-item` (the shop tiles), and
`desktop-header-shop-drawer`. It also renders the desktop currency selector.

## Where it's used

Lives in **both** header section groups (`header-group.json`,
`header-group-no-background.json`), so it's on every page whose layout includes a
header group. The two groups differ mainly in `does-header-have-background` and text
colors. Preset category: **Header Group**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `does-header-have-background` | Does Header Have Background? | checkbox | `true` |
| `text-color` | Text Color | color | `#111111` |
| `text-hover-color` | Text Hover Color | color (alpha) | `#111111` |
| `active-shop-drawer-inactive-text-color` | Inactive Text Color when Shop Drawer Active | color (alpha) | `rgba(17,17,17,0.5)` |
| `desktop--shop-menu-item-padding` | Desktop Shop Menu Item Padding | number | `8` |
| `restock-alert-page` | Restock Alert page | page | — |
| `restock-alert-menu-label` | Restock Alert menu label | text | `GET UPDATES` |

Menu **links** are not here — they're global theme settings (`Header Menu` and
`Header Sidebar` groups: `header-left-menu`, `header-right-menu`,
`header-sidebar-main-menu`, `header-sidebar-soon-menu`, plus the menu-item title and
header background-color settings).

## Metafields & metaobjects

None.

## Snippets rendered

- `desktop-currency-selector` — the localization (country/currency) selector form.

## Notes

- Header height feeds `--sm--header-menu-height` in `snippets/css-variables.liquid`;
  layout math elsewhere depends on it.
- `does-header-have-background` is the key difference between the two header groups —
  the no-background variant is used by the homepage and cover pages so the hero shows
  through.
- The shop tiles in the drawer (`header-shop-item` blocks) each carry their own image
  and link; they're configured per block, not in section settings.
