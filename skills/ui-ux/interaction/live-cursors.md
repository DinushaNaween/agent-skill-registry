---
id: ui-ux.interaction.live-cursors
name: Live Cursors
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Three cursors land on your canvas. None of them are yours.
triggers:
- designing or building live cursors components
- reviewing UX/UI for live cursors
- implementing interaction pattern for live cursors
- three cursors land on your canvas
tags:
- ui
- ux
- interaction
- live
- cursors
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-20'
---

# Live Cursors

> Three cursors land on your canvas. None of them are yours.

## When to Use (Triggers)

- designing or building live cursors components
- reviewing UX/UI for live cursors
- implementing interaction pattern for live cursors
- three cursors land on your canvas

## Key Insights & Principles

- The server streams roughly10 positions a secondwhile the screen redraws at 60fps.Interpolationfills the gaps so cursors glide instead of teleporting between discrete points.
- Give every user a colorhashed from their ID, not assigned at random. The same person keeps the same color across sessions, so you can track identity from the corner of your eye.
- Anavatar stackwith an overflow counter (three faces, then a +5) signals presence before anyone edits or speaks. You feel the room before you read a single name.
- When someone selects an element,lock itand outline it in their color. Two people editing one shape is a corrupted shape, so the lock prevents the conflict before it can exist.
- Follow modebinds your viewport to another user's: click their avatar and their pans and zooms drive your screen. It replaces a screen share for live design review.

## Do's and Don'ts

- **Do:** Interpolate cursor positions between server ticks so movement reads as smooth motion at 60fps.
- **Do:** Derive user color from a stable hash of the ID so it survives across sessions.
- **Do:** Lock an element the instant it is selected and badge it in the editor's color.
- **Don't:** Render cursors at the raw server tick rate, which makes them jump between points.
- **Don't:** Assign colors randomly per session, which resets identity every time someone rejoins.
- **Don't:** Allow two users to edit the same element at once.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
