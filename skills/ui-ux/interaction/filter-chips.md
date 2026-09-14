---
id: ui-ux.interaction.filter-chips
name: Filter Chips
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: 200 results. Three taps. 12 left.
triggers:
- designing or building filter chips components
- reviewing UX/UI for filter chips
- implementing interaction pattern for filter chips
- 200 results
tags:
- ui
- ux
- interaction
- filter
- chips
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-08'
---

# Filter Chips

> 200 results. Three taps. 12 left.

## When to Use (Triggers)

- designing or building filter chips components
- reviewing UX/UI for filter chips
- implementing interaction pattern for filter chips
- 200 results

## Key Insights & Principles

- Give every chip three distinct visual states —idle(surface + border, tappable but not chosen),active(filled + check, clearly selected), anddisabled(dimmed, no results behind it). If active looks like idle, the filter feels broken.
- Make the combination logic legible:OR within a groupwidens the net (more colors = more matches),AND across groupsnarrows it (adding a size filters the set down).
- Update the result count on thesame frameas the tap. If the number doesn't move, users read it as 'nothing happened' and tap twice.
- Always ship a singleclear-allreset. Stacked filters trap users, and one tap back to zero is the escape hatch — pair it with a live count so the reset is legible.
- When chips outrun the screen, keep them inone horizontal scrolling rowwith a right-edge fade that hints at more. Wrapping into a multi-row wall buries the results below the fold.
- Pin active filters in asticky summary baron top so users can always see why the list shrank.

## Do's and Don'ts

- **Do:** Update the result count instantly on every tap, same frame as the state change
- **Do:** Give each chip clearly distinct idle, active, and disabled states
- **Do:** Offer a single clear-all reset paired with a live result count
- **Don't:** Let active chips look identical to idle ones — the filter reads as broken
- **Don't:** Wrap overflowing chips into a multi-row wall that pushes results off-screen
- **Don't:** Leave the count unchanged after a tap — users assume it failed and tap again
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
