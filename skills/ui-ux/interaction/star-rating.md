---
id: ui-ux.interaction.star-rating
name: Star Rating
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Five stars looks trivial. Hover, half-fills, and honest averages are where it breaks.
triggers:
- designing or building star rating components
- reviewing UX/UI for star rating
- implementing interaction pattern for star rating
- five stars looks trivial
tags:
- ui
- ux
- interaction
- star
- rating
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/star-rating
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Star Rating

> Five stars looks trivial. Hover, half-fills, and honest averages are where it breaks.

## When to Use (Triggers)

- designing or building star rating components
- reviewing UX/UI for star rating
- implementing interaction pattern for star rating
- five stars looks trivial

## Key Insights & Principles

- Preview on hover, don't wait for the click. Stars should fill ahead of the cursor so users see the value they're about to commit — a widget that only reacts on click hides the target until it's too late.
- Keep thepreview state separate from the committed value. When the pointer leaves without clicking, snap the display back to the saved rating; a naive build leaves it stuck on the last hovered star.
- For averages, renderfractional stars— a 4.4 is four full stars plus a fifth clipped to 44%. Rounding it up to five full stars is a lie that inflates perceived quality.
- Stagger the fill ~30ms per star, left to right. Popping all five at once feels flat and lifeless; the sequential sweep feels alive.
- Use fractional fill for input precision too — clumsy whole-star jumps read as cheap next to a smooth half-star land.
- Stars are the input; pair them with asummary view(an average ring plus a distribution breakdown) to communicate the aggregate score at a glance.

## Do's and Don'ts

- **Do:** Fill stars ahead of the cursor on hover so the value previews before commit
- **Do:** Render partial fills so a 4.4 shows four stars plus a 44%-filled fifth
- **Do:** Stagger the fill roughly 30ms per star, left to right, when a rating commits
- **Don't:** Round averages up to full stars — it misrepresents the real score
- **Don't:** Leave the preview stuck on the hovered value after the pointer leaves
- **Don't:** Pop all five stars simultaneously — it reads as flat and dead
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/star-rating.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/star-rating.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/star-rating)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
