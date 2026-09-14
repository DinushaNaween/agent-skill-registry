---
id: ui-ux.feedback.loading-states-system
name: Loading States System
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Stop using skeletons for everything. Loading is a system, not a default.
triggers:
- designing or building loading states system components
- reviewing UX/UI for loading states system
- implementing feedback pattern for loading states system
- stop using skeletons for everything
tags:
- ui
- ux
- feedback
- loading
- states
- system
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.notification-system
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/loading-states-system
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Loading States System

> Stop using skeletons for everything. Loading is a system, not a default.

## When to Use (Triggers)

- designing or building loading states system components
- reviewing UX/UI for loading states system
- implementing feedback pattern for loading states system
- stop using skeletons for everything

## Key Insights & Principles

- Loading is a system: match the pattern to what you actually know about the wait — its shape, its duration, its progress. One default (usually a skeleton) applied everywhere is the tell of a lazy UI.
- Skeletonsare for when you know the content's shape — cards, lists, articles — and the wait exceeds ~300ms. They set the right expectation by previewing the layout that's about to load.
- Spinnersfit short waits of unknown duration, under ~3s (a button saving, a small fetch). Never stretch one across a full-page load — an endless spinner with no context reads as frozen.
- Progress barsbelong to waits over ~3s where you know the percentage — uploads, installs, exports. Pair the bar with real meta (time remaining, speed) so the number earns the user's trust.
- Optimistic UIis the pro move for reversible actions like likes, saves, and bookmarks: update the interface instantly, then reconcile with the server in the background and only surface an error if the sync fails.
- Under ~300ms,show nothing at all. A brief flash of a loading state feels more broken than a slight delay — the eye registers the flicker as a glitch, not as feedback.

## Do's and Don'ts

- **Do:** Pick the pattern from what you know: known shape → skeleton, known percentage → progress, short unknown wait → spinner.
- **Do:** Apply the response instantly for reversible actions, then sync in the background and roll back only on failure.
- **Do:** Let sub-300ms responses land with no loading indicator at all.
- **Don't:** Reach for a skeleton on every fetch regardless of the content shape or how long it takes.
- **Don't:** Cover a whole page with a spinner for long or open-ended loads.
- **Don't:** Flash any loading state for a response that resolves in under 300ms.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/loading-states-system.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/loading-states-system.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/loading-states-system)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.notification-system`
