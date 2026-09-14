---
id: ui-ux.feedback.error-states
name: Error States
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Same error. Better recovery.
triggers:
- designing or building error states components
- reviewing UX/UI for error states
- implementing feedback pattern for error states
- same error
tags:
- ui
- ux
- feedback
- error
- states
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.loading-states-system
- ui-ux.feedback.notification-system
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/error-states
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Error States

> Same error. Better recovery.

## When to Use (Triggers)

- designing or building error states components
- reviewing UX/UI for error states
- implementing feedback pattern for error states
- same error

## Key Insights & Principles

- Match the error type to its surface.A validation error belongs inline under the field, a lost connection reads as a banner or toast, and a server crash or permission block needs its own prominent space — each type has a natural home.
- Let severity drive the surface.Minor issues stay inline, transient ones surface as a toast, and blocking failures earn a modal. The more an error interrupts the user, the more space it should occupy — and the reverse.
- Every error needs an exit.A dead-end 'OK' button leaves people stuck. Give a real way out — aRetry, a link to support, or expandable technical details for those who want to dig in.
- Write copy for humans, not machines.'Error 500 — An error occurred' tells the user nothing. Say what broke, why, and what to do next in plain, specific language.
- Prevent errors before they happen.Live inline validation — checking each rule as the user types and turning criteria green — stops most mistakes before submit. Validating only on submit just tells people they failed after the fact.
- Keep field-level validationsmall, inline, and specific— anchored to the input it describes, not floating in a generic alert.

## Do's and Don'ts

- **Do:** Offer a clear recovery action on every error — retry, undo, or a path to help.
- **Do:** Match the surface to severity: inline for field errors, toast for transient issues, modal for true blockers.
- **Do:** Validate inline as the user types so problems surface before submit.
- **Don't:** Ship dead-end errors whose only option is 'OK'.
- **Don't:** Surface raw codes like 'Error 500' or 'An error occurred' with no guidance.
- **Don't:** Interrupt a minor validation slip with a full-screen modal.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/error-states.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/error-states.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/error-states)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.loading-states-system`
- `ui-ux.feedback.notification-system`
