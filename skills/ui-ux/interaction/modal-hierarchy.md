---
id: ui-ux.interaction.modal-hierarchy
name: Modal Hierarchy
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: 5 overlays. Most apps pick the wrong one.
triggers:
- designing or building modal hierarchy components
- reviewing UX/UI for modal hierarchy
- implementing interaction pattern for modal hierarchy
- 5 overlays
tags:
- ui
- ux
- interaction
- modal
- hierarchy
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-04-30'
---

# Modal Hierarchy

> 5 overlays. Most apps pick the wrong one.

## When to Use (Triggers)

- designing or building modal hierarchy components
- reviewing UX/UI for modal hierarchy
- implementing interaction pattern for modal hierarchy
- 5 overlays

## Key Insights & Principles

- Start with one question:does it block the user?If yes, reach for a modal; if no, choose by context — sheet, popover, or drawer.
- Amodaltakes over the screen with a full scrim and centers a single decision. Reserve it for critical or destructive choices (like "Delete account?") that must be answered before anything else.
- Abottom sheetis the mobile-first default: it slides up from the bottom edge, supports a drag handle and snap points, and keeps the screen behind it partly visible so users don't lose context.
- Adraweris an edge-anchored panel for navigation — it slides in from the side, dims only the area it covers, and leaves the app alive behind it.
- Apopoveranchors to the element that triggered it and stays small and contextual (~200px). Use it for lightweight menus and quick actions, never for blocking flows.
- Matchweight to intent: modals interrupt, popovers and sheets stay non-blocking. Reaching for a modal when a popover would do adds friction to routine actions.

## Do's and Don'ts

- **Do:** Ask "does this block the user?" before picking any overlay.
- **Do:** Reserve modals for critical or destructive decisions that demand a response.
- **Do:** Anchor popovers to their trigger and keep them small and contextual.
- **Don't:** Reach for a modal when a lightweight sheet or popover would do the job.
- **Don't:** Use a full-screen scrim for a routine, non-blocking action.
- **Don't:** Bury navigation inside a blocking overlay — use an edge drawer instead.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
