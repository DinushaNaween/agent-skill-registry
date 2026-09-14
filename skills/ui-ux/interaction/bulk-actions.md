---
id: ui-ux.interaction.bulk-actions
name: Bulk Actions
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Bulk actions are a system, not a lone checkbox.
triggers:
- designing or building bulk actions components
- reviewing UX/UI for bulk actions
- implementing interaction pattern for bulk actions
- bulk actions are a system, not a lone checkbox
tags:
- ui
- ux
- interaction
- bulk
- actions
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.disabled-buttons
- ui-ux.interaction.hover-trap
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-08-09'
---

# Bulk Actions

> Bulk actions are a system, not a lone checkbox.

## When to Use (Triggers)

- designing or building bulk actions components
- reviewing UX/UI for bulk actions
- implementing interaction pattern for bulk actions
- bulk actions are a system, not a lone checkbox

## Key Insights & Principles

- The header checkbox needsthree states: empty, partial, and checked. The indeterminate dash is not optional, and partial always resolves to select-all, never to clear.
- Name the number.When select-all only grabs the rows on screen, offer 'Select all 247 matching' instead of a bare 'all' that hides the true scope.
- Keep the count honest as context shifts. Change a filter and the label should re-read live (from 247 matching down to 96) so people act on the real set.
- Selection is state, not the DOM.Shift-click picks a range, and the selected ids survive paging because they live in application state, not in the visible rows.
- For destructive bulk actions, skip the confirm modal.Echo the count, run the action immediately, and offer a 10 second undo with a draining countdown ring.

## Do's and Don'ts

- **Do:** Give the header checkbox all three states and let the partial dash resolve to select-all.
- **Do:** Spell out the exact count in the affordance, like 'Select all 247 matching'.
- **Do:** Swap destructive confirm dialogs for an undo window that echoes what you deleted.
- **Don't:** Ship a two-state header checkbox that skips the indeterminate dash.
- **Don't:** Label bulk selection with a vague 'all' that hides how many rows you touched.
- **Don't:** Store the selection in the DOM, where it silently resets the moment someone changes page.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.disabled-buttons`
- `ui-ux.interaction.hover-trap`
