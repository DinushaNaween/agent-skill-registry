---
id: ui-ux.interaction.dropdown-design
name: Dropdown Design
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Your dropdown is broken. Five rules separate cheap from premium.
triggers:
- designing or building dropdown design components
- reviewing UX/UI for dropdown design
- implementing interaction pattern for dropdown design
- your dropdown is broken
tags:
- ui
- ux
- interaction
- dropdown
- design
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Dropdown Design

> Your dropdown is broken. Five rules separate cheap from premium.

## When to Use (Triggers)

- designing or building dropdown design components
- reviewing UX/UI for dropdown design
- implementing interaction pattern for dropdown design
- your dropdown is broken

## Key Insights & Principles

- Make the triggerobviously clickable: a 48px touch target, a visible caret icon, and a real hover state — not a 30px box with a faint border.
- Flip on edge— when there isn't enough room below the trigger, open the menu upward so it never clips off-screen.
- Keyboard support isn't optional: arrow keys move the highlight, Enter selects the item, and Esc closes the menu.
- Once a list passes~10 items, add a search field so users filter instead of scroll-hunting.
- Animate the open in around150ms— 50ms feels instant and cheap, 500ms drags and feels sluggish.

## Do's and Don'ts

- **Do:** Give the trigger a 48px touch target, a clear caret, and a visible hover state.
- **Do:** Open the menu upward when space below the trigger runs out.
- **Do:** Wire up arrow keys, Enter, and Esc for full keyboard control.
- **Don't:** Ship a 30px, low-contrast trigger with no hover feedback.
- **Don't:** Let a long menu clip off the bottom of the viewport.
- **Don't:** Animate slower than ~150ms — or with no transition at all.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
