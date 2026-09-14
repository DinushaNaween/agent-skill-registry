---
id: ui-ux.feedback.notification-system
name: Notification System
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Notifications are a system. Pick the wrong surface and users tune out.
triggers:
- designing or building notification system components
- reviewing UX/UI for notification system
- implementing feedback pattern for notification system
- notifications are a system
tags:
- ui
- ux
- feedback
- notification
- system
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/notification-system
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Notification System

> Notifications are a system. Pick the wrong surface and users tune out.

## When to Use (Triggers)

- designing or building notification system components
- reviewing UX/UI for notification system
- implementing feedback pattern for notification system
- notifications are a system

## Key Insights & Principles

- A notification isn't one component — it's asystem of four surfaces: toast, banner, modal, and badge. The same content can be delivered at four different volumes.
- The trigger picks the volume.Let the event's severity decide the surface: a low-priority "new message" fits a toast, a degraded-service warning a banner, a blocking "card declined" error a modal, and a passive unread count a badge.
- Persistence is part of the contract.Toasts auto-dismiss in a few seconds (and should offer undo), banners stay until manually cleared, modals block until the user acts, and badges sit quietly until the count is resolved.
- Stack behavior separates good from broken.Several toasts can stack and breathe; several modals become a trainwreck — blocking dialogs must never queue on top of each other.
- Over-escalating backfires: route everything to the loudest surface and you getzero attention, because users learn to tune the noise out.

## Do's and Don'ts

- **Do:** Map each notification's severity to the surface that matches it — toast, banner, modal, or badge.
- **Do:** Let toasts auto-dismiss with an undo affordance, and reserve modals for actions that genuinely must block.
- **Do:** Stack low-priority notifications so they breathe instead of piling up on screen.
- **Don't:** Route every alert to the most intrusive surface — over-escalation trains users to ignore all of them.
- **Don't:** Queue multiple modals on top of each other; blocking dialogs stacked together are a trainwreck.
- **Don't:** Use a blocking modal for a low-severity, purely informational message.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/notification-system.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/notification-system.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/notification-system)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
