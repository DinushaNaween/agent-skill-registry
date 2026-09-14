---
id: ui-ux.feedback.optimistic-ui
name: Optimistic UI
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Click like. One waits. One feels instant.
triggers:
- designing or building optimistic ui components
- reviewing UX/UI for optimistic ui
- implementing feedback pattern for optimistic ui
- click like
tags:
- ui
- ux
- feedback
- optimistic
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-26'
---

# Optimistic UI

> Click like. One waits. One feels instant.

## When to Use (Triggers)

- designing or building optimistic ui components
- reviewing UX/UI for optimistic ui
- implementing feedback pattern for optimistic ui
- click like

## Key Insights & Principles

- Update the UI the instant the user acts, thensync with the server in the background— don't block on the response.
- The brain reads anything under400msas instant; a spinner past that threshold makes the action feel broken.
- When the request fails,roll backthe UI cleanly — undo the like, restore the count, as if it never happened.
- The core bet: trust thesuccess case(which is almost always what happens) and handle the rare failure gracefully.
- Reserve it forreversible, low-stakes actions— likes, toggles, reorders — where an occasional rollback costs nothing.

## Do's and Don'ts

- **Do:** Update the interface immediately, then reconcile with the real server response behind the scenes.
- **Do:** Roll back to the previous state the moment a request fails, so the UI never lies for long.
- **Do:** Apply it to reversible interactions like likes, favorites, and list reordering.
- **Don't:** Use it for payments, transfers, or anything you can't safely undo.
- **Don't:** Show a charge, booking, or confirmation before the server has actually cleared it.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
