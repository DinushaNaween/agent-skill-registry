---
id: ui-ux.feedback.undo-ux
name: Undo UX
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Deleted. You have five seconds.
triggers:
- designing or building undo ux components
- reviewing UX/UI for undo ux
- implementing feedback pattern for undo ux
- deleted
tags:
- ui
- ux
- feedback
- undo
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-03'
---

# Undo UX

> Deleted. You have five seconds.

## When to Use (Triggers)

- designing or building undo ux components
- reviewing UX/UI for undo ux
- implementing feedback pattern for undo ux
- deleted

## Key Insights & Principles

- Undo beats confirmation."Are you sure?" punishes everyone for one person's mistake; undo punishes nobody. The action happens instantly, and regret gets a second chance.
- Soft deletemeans the file left the screen, not the database. Set a deleted flag, keep it in trash for thirty days, then purge. Deletion is a state, not an event.
- Friction belongs only where there's no way back.For truly irreversible actions, make users earn it — GitHub requires typing the repo name before deleting it.
- One undo is a toast; a stack is a time machine.An undo stack lets Cmd+Z walk back through every step in order, the way Figma remembers everything you did.
- Delayed send turns a delay into a feature.Gmail holds your email for ten seconds after send — long enough to catch the typo, the wrong recipient, or the reply-all disaster.
- Show the countdown.A visible timer on the undo toast (a draining ring or bar) tells users exactly how long their second chance lasts.

## Do's and Don'ts

- **Do:** Execute the action immediately, then offer a time-limited undo with a visible countdown
- **Do:** Soft-delete with a recovery window (e.g. 30 days in trash) before permanent purge
- **Do:** Reserve heavy friction like type-to-confirm for genuinely irreversible actions
- **Don't:** Block every destructive action behind an "Are you sure?" dialog
- **Don't:** Hard-delete data from the database the moment the user clicks
- **Don't:** Make the undo window so short users can't realistically react
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
