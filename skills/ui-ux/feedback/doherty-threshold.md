---
id: ui-ux.feedback.doherty-threshold
name: Doherty Threshold
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Cross 400ms and your user checks out. Perceived speed is a design choice.
triggers:
- designing or building doherty threshold components
- reviewing UX/UI for doherty threshold
- implementing feedback pattern for doherty threshold
- cross 400ms and your user checks out
tags:
- ui
- ux
- feedback
- doherty
- threshold
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
- ui-ux.feedback.notification-system
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/doherty-threshold
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Doherty Threshold

> Cross 400ms and your user checks out. Perceived speed is a design choice.

## When to Use (Triggers)

- designing or building doherty threshold components
- reviewing UX/UI for doherty threshold
- implementing feedback pattern for doherty threshold
- cross 400ms and your user checks out

## Key Insights & Principles

- TheDoherty Thresholdis 400ms: respond faster and you hold attention, respond slower and users mentally disconnect.
- Response time splits into zones —under 200msfeels instant,200–400msis tolerable, andover 400msstarts breaking engagement.
- What matters isperceivedspeed, not raw speed — the real work can take longer as long as the interface reacts within the threshold.
- Skeleton loadingpaints placeholder shapes the instant a screen opens, so it never looks frozen while data arrives.
- Optimistic UIupdates the screen as if the action already succeeded, then reconciles only if the server rejects it.
- Progress feedback— spinners, progress bars, inline status — keeps an unavoidable wait feeling responsive instead of stalled.

## Do's and Don'ts

- **Do:** Give visible feedback within 400ms of any interaction, even if it's just a skeleton or acknowledgment
- **Do:** Update the interface optimistically for actions that almost always succeed
- **Do:** Show progress feedback whenever the real work has to exceed the threshold
- **Don't:** Leave the screen blank or frozen while data loads in the background
- **Don't:** Wait for a server round-trip before giving any visual response
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/doherty-threshold.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/doherty-threshold.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/doherty-threshold)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
- `ui-ux.feedback.notification-system`
