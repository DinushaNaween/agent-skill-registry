---
id: ui-ux.forms.form-field-states
name: Form Field States
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Six field states, one system. Miss one and you ship a bug.
triggers:
- designing or building form field states components
- reviewing UX/UI for form field states
- implementing forms pattern for form field states
- six field states, one system
tags:
- ui
- ux
- forms
- form
- field
- states
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.autosave-ux
- ui-ux.forms.date-pickers
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Form Field States

> Six field states, one system. Miss one and you ship a bug.

## When to Use (Triggers)

- designing or building form field states components
- reviewing UX/UI for form field states
- implementing forms pattern for form field states
- six field states, one system

## Key Insights & Principles

- A text field hassix states— default, focus, error, success, disabled, and loading — and each needs an explicit design. Forget one and it becomes a bug in production.
- At rest, keep thelabel outsidethe field with helper text below it. A placeholder-as-label vanishes the moment someone starts typing.
- On focus, make the active target obvious with afocus ring of at least 3:1 contrast. A soft blue glow looks pretty but fails accessibility checks.
- For errors, combinecolor + icon + messagetogether — a border-only red is invisible to the ~12% of users with color-vision deficiency. Name what's wrong and how to fix it.
- Confirm successinside the field, where the user's attention already is. Toasts steal focus and disappear before they're read.
- Keepdisabled and loading visually distinct: disabled uses a grayscale fill with a not-allowed cursor, while loading shows an in-field spinner and blocks input to prevent double submits.

## Do's and Don'ts

- **Do:** Place the label above the field and helper text below, so nothing disappears on input
- **Do:** Signal every error with color, an icon, and a written message at once
- **Do:** Disable the input and show a spinner during async checks to stop double submits
- **Don't:** Use a placeholder as the label — it vanishes as soon as typing begins
- **Don't:** Rely on a border-only red for errors; roughly 12% of users won't perceive it
- **Don't:** Fake a disabled state with opacity 0.5 — it reads as a loading state instead
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.autosave-ux`
- `ui-ux.forms.date-pickers`
