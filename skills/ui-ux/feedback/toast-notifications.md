---
id: ui-ux.feedback.toast-notifications
name: Toast Notifications
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: 'Toasts done right: five rules for notifications that inform without blocking.'
triggers:
- designing or building toast notifications components
- reviewing UX/UI for toast notifications
- implementing feedback pattern for toast notifications
- 'toasts done right: five rules for notifications that inform without blocking'
tags:
- ui
- ux
- feedback
- toast
- notifications
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Toast Notifications

> Toasts done right: five rules for notifications that inform without blocking.

## When to Use (Triggers)

- designing or building toast notifications components
- reviewing UX/UI for toast notifications
- implementing feedback pattern for toast notifications
- toasts done right: five rules for notifications that inform without blocking

## Key Insights & Principles

- Positiondeliberately: bottom-right on desktop, top edge on mobile. The screencenter is off-limits— it covers the content users are actively working on and blocks clicks.
- Match dismisstiming to severity: routine info auto-dismisses in ~4s, warnings hold ~7s, and critical errors stayuntil the user acknowledgesthem.
- Cap the stack at3 visibletoasts — newest enters at the bottom, older ones float up and out, and the rest queue. Spring motion keeps the shuffle readable.
- Always give away out: a close button on desktop, swipe-to-dismiss on mobile, and a timer thatpauses on hoverso people can finish reading.
- Color-code by type (info, success, warning, error) butnever rely on color alone— pair each with an icon and accent border, since ~6% of users can't tell the colors apart.

## Do's and Don'ts

- **Do:** Anchor toasts bottom-right on desktop and to the top edge on mobile
- **Do:** Pause the auto-dismiss countdown while the user hovers so they have time to read
- **Do:** Reinforce each type's color with a matching icon and left accent border
- **Don't:** Place toasts in the screen center, where they block the content users are working on
- **Don't:** Auto-dismiss critical errors — hold them until the user acknowledges
- **Don't:** Show more than three toasts at once; queue the rest instead of piling them up
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
