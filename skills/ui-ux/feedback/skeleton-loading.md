---
id: ui-ux.feedback.skeleton-loading
name: Skeleton Loading
version: 1.0.0
domain: ui-ux
subdomain: feedback
summary: Your loading spinner is making the wait feel longer
triggers:
- designing or building skeleton loading components
- reviewing UX/UI for skeleton loading
- implementing feedback pattern for skeleton loading
- your loading spinner is making the wait feel longer
tags:
- ui
- ux
- feedback
- skeleton
- loading
priority: medium
dependencies: []
related_skills:
- ui-ux.feedback.doherty-threshold
- ui-ux.feedback.error-states
- ui-ux.feedback.loading-states-system
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/skeleton-loading
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-06-15'
---

# Skeleton Loading

> Your loading spinner is making the wait feel longer

## When to Use (Triggers)

- designing or building skeleton loading components
- reviewing UX/UI for skeleton loading
- implementing feedback pattern for skeleton loading
- your loading spinner is making the wait feel longer

## Key Insights & Principles

- A spinner tells users "something is happening" but gives zero information aboutwhatorhow long. That uncertainty is what makes waits feel slow.
- Skeleton screens preview the shape of the incoming content — avatar circle, text bars, image block — so the brain starts parsing the layout before the data arrives.
- The shimmer sweep matters: a static skeleton reads as "broken", an animated one reads as "in progress".
- Match the skeleton to the real content dimensions. A skeleton that jumps to a different layout on load is worse than a spinner.
- For actions the user just performed (posting, liking), skip loading states entirely — render the result optimistically and reconcile in the background.

## Do's and Don'ts

- **Do:** shape skeletons to mirror the final layout, animate them, and keep them under ~2 seconds before showing partial content.
- **Don't:** use skeletons for sub-300ms loads (flash of skeleton is noise) or mix spinners and skeletons in the same view.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/skeleton-loading.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/skeleton-loading.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/skeleton-loading)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.feedback.doherty-threshold`
- `ui-ux.feedback.error-states`
- `ui-ux.feedback.loading-states-system`
