---
id: ui-ux.forms.date-pickers
name: Date Pickers
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Same date. Six clicks. Or one. The picker that respects your users' time.
triggers:
- designing or building date pickers components
- reviewing UX/UI for date pickers
- implementing forms pattern for date pickers
- same date
tags:
- ui
- ux
- forms
- date
- pickers
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.autosave-ux
- ui-ux.forms.form-field-states
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/date-pickers
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Date Pickers

> Same date. Six clicks. Or one. The picker that respects your users' time.

## When to Use (Triggers)

- designing or building date pickers components
- reviewing UX/UI for date pickers
- implementing forms pattern for date pickers
- same date

## Key Insights & Principles

- Presets cover ~90% of cases.Offer Today, Yesterday, Last 7 days, Last 30 days, and Last quarter as one-click options, and reserve acustom rangefor the remaining edge cases.
- For custom ranges, make selection legible:hovering paints a live preview, the first click locks the start, the second locks the end, and the edges staydraggableto refine without starting over.
- Show two months side by sideso a range can cross the month boundary naturally — never force users to click "next" four times to reach a nearby date. Widen to three months on large screens.
- Support thefull keyboard: arrows move focus across the grid, users can type the date directly, Enter confirms, Escape closes, Page Up jumps a month, and Shift+Page Up jumps a year.
- Mobile is not a popover.Use a full-screen sheet that scrolls vertically, keep today anchored at the top, and place a large confirm button at the bottom within thumb reach.

## Do's and Don'ts

- **Do:** Lead with presets for common ranges and keep a custom option only for the exceptions
- **Do:** Render two calendar months at once so ranges can span the month boundary
- **Do:** Wire up the full keyboard — typing, arrow navigation, Enter/Escape, and month/year jumps
- **Don't:** Force repeated "next" clicks to reach a month that's only a few weeks away
- **Don't:** Shrink the desktop popover onto mobile instead of using a full-screen sheet
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/date-pickers.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/date-pickers.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/date-pickers)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.autosave-ux`
- `ui-ux.forms.form-field-states`
