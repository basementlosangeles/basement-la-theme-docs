# Contact

`sections/contact.liquid`

## What it does

The Contact page form — title, rich-text intro, and the name/email/subject/message
inputs with placeholder and error copy, plus submit text. All field labels and
helper text are merchant-editable.

## Where it's used

Assigned in `templates/page.Contact.json`, using the `page-cover-theme` layout. The
template attaches a single `featured-cover-image` block (`max_blocks: 1`). Preset
name: **Contact**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `title-text` | Title Text | text | `Get in Touch` |
| `body-text` | Body Text | richtext | `<p>Please fill in the form below or email us at <strong>getbasement@gmail.com.</strong></p>` |
| `name-input-placeholder-text` | Name Input Placeholder | text | `Name` |
| `subject-input-placeholder-text` | Subject Input Placeholder | text | `SUBJECT (ORDER NUMBER IF APPLICABLE)` |
| `message-input-placeholder-text` | Message Input Placeholder | text | `Message` |
| `email-input-placeholder-text` | Email Input Placeholder | text | `Email` |
| `email-input-error-text` | Email Input Error Text | text | `Enter a valid email!` |
| `submit-text` | Submit Text | text | `All fields are required to submit.` |
| `submit-btn-text` | Submit Button Text | text | `Submit` |

Accepts one block: `"blocks": [{ "type": "@theme" }]`, `"max_blocks": 1`.

## Metafields & metaobjects

None.

## Snippets rendered

None.

## Notes

- `body-text` is `richtext`, so it stores HTML — the default includes a `<strong>`
  email address. Editing it through the editor preserves formatting.
- The contact email shown to shoppers is content, not a setting — it's embedded in
  `body-text`.
