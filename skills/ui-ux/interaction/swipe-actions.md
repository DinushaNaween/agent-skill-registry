---
id: ui-ux.interaction.swipe-actions
name: Swipe Actions
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Your swipe actions are killing your UX
triggers:
- designing or building swipe actions components
- reviewing UX/UI for swipe actions
- implementing interaction pattern for swipe actions
- your swipe actions are killing your ux
tags:
- ui
- ux
- interaction
- swipe
- actions
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-03'
---

# Swipe Actions

> Your swipe actions are killing your UX

## When to Use (Triggers)

- designing or building swipe actions components
- reviewing UX/UI for swipe actions
- implementing interaction pattern for swipe actions
- your swipe actions are killing your ux

## Key Insights & Principles

- Swipe actions are invisible UI. Without an affordance hint (a peek of the action on first scroll, an onboarding nudge), most users never discover them.
- Destructive swipes need friction: a full swipe that instantly deletes is a data-loss bug waiting to happen. Reveal the button on partial swipe, require a tap (or full-swipe + undo toast) to commit.
- Color-code by consequence: neutral actions on surface tones, destructive on red — and keep the mapping consistent across every list in the app.
- Never make swipe the only path. Every swipe action needs a visible fallback (long-press menu, detail-view button) for discoverability and accessibility.

## Do's and Don'ts

- **Do:** pair each swipe action with an undo window, and keep left/right semantics consistent app-wide.
- **Don't:** hide more than two actions per side — beyond that, users can't build muscle memory.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
