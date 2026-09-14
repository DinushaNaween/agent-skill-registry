---
id: ui-ux.navigation.pagination
name: Pagination
version: 1.0.0
domain: ui-ux
subdomain: navigation
summary: Add one row and your pagination breaks.
triggers:
- designing or building pagination components
- reviewing UX/UI for pagination
- implementing navigation pattern for pagination
- add one row and your pagination breaks
tags:
- ui
- ux
- navigation
- pagination
priority: medium
dependencies: []
related_skills:
- ui-ux.navigation.navigation-patterns
- ui-ux.navigation.tabs-system
- ui-ux.navigation.focus-states
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-08'
---

# Pagination

> Add one row and your pagination breaks.

## When to Use (Triggers)

- designing or building pagination components
- reviewing UX/UI for pagination
- implementing navigation pattern for pagination
- add one row and your pagination breaks

## Key Insights & Principles

- Offset paginationdrifts when the data changes — insert a row at the top and every page shifts down, so the same item can surfacetwice(or get skipped entirely).
- Cursor paginationstays stable: it anchors to a specific row instead of a numeric position, so inserts and deletes never create duplicates.
- Three patterns fit different jobs —numberedfor jumping to any page,load-morefor on-demand appends,infinite scrollfor continuous feeds.
- Never render every page link.Truncateto first, last, current, and its immediate neighbors, using an ellipsis for the gaps.
- Keep the page numberin the URL(?page=500) so a refresh stays put and the view becomes a shareable link.
- When users return from a detail view,restore their scroll positioninstead of dumping them back at the top of the list.

## Do's and Don'ts

- **Do:** Reach for cursor pagination when rows are inserted or deleted often, to avoid duplicates and skips
- **Do:** Persist the current page in the URL so refreshes and shared links land on the same page
- **Do:** Collapse long page ranges to first, last, current, and neighbors with an ellipsis
- **Don't:** Render hundreds of numbered links — they spill off-screen and overwhelm
- **Don't:** Reset an infinite-scroll list to the top when the user comes back from a detail view

## Code & Selectors

```css
?page=500
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.navigation.navigation-patterns`
- `ui-ux.navigation.tabs-system`
- `ui-ux.navigation.focus-states`
