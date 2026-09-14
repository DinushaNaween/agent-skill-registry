---
id: ui-ux.interaction.data-table
name: Data Table
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Your data table feels cheap because it's a grid of divs, not a system.
triggers:
- designing or building data table components
- reviewing UX/UI for data table
- implementing interaction pattern for data table
- your data table feels cheap because it's a grid of divs, not a system
tags:
- ui
- ux
- interaction
- data
- table
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/data-table
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-05-29'
---

# Data Table

> Your data table feels cheap because it's a grid of divs, not a system.

## When to Use (Triggers)

- designing or building data table components
- reviewing UX/UI for data table
- implementing interaction pattern for data table
- your data table feels cheap because it's a grid of divs, not a system

## Key Insights & Principles

- Sort is atri-state, not a toggle: ascending → descending → back to original. A binary flip loses the natural order forever; a third click should restore it.
- Numbers must line up — usetabular figuresandright-alignnumeric columns so every digit sits on the same grid. Proportional, left-aligned digits jitter and can't be compared at a glance.
- Freeze what you navigate by: keep theheader stickyon vertical scroll andfreeze the first columnon horizontal scroll, each with a subtle shadow so labels never scroll out of reach.
- Treatdensity as a token, not a guess — one control switching row heights (e.g. 36 / 48 / 60px) gives a predictable rhythm. Zebra stripes help at comfortable spacing; collapse to a single hairline as rows compact.
- Make thewhole rowthe selection target — full tint + an accent left bar + the checkbox — instead of a tiny checkbox-only hit area that's easy to miss.
- Signal partial selection with aselect-allstate that morphs empty → indeterminate (dash) → checked, so bulk actions read at a glance.

## Do's and Don'ts

- **Do:** Right-align numeric columns with tabular figures so values form a scannable vertical grid.
- **Do:** Keep the header sticky and freeze the first column so labels stay anchored while scrolling.
- **Do:** Expose row density as one token-driven control for consistent, predictable spacing.
- **Don't:** Ship a binary sort that strips the original order with no way back to natural sequence.
- **Don't:** Rely on a tiny checkbox-only hit target when the entire row could be clickable.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/data-table.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/data-table.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/data-table)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
