---
id: ui-ux.interaction.bottom-sheets
name: Bottom Sheets
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Your thumb can't reach that menu.
triggers:
- designing or building bottom sheets components
- reviewing UX/UI for bottom sheets
- implementing interaction pattern for bottom sheets
- your thumb can't reach that menu
tags:
- ui
- ux
- interaction
- bottom
- sheets
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/bottom-sheets
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-06-26'
---

# Bottom Sheets

> Your thumb can't reach that menu.

## When to Use (Triggers)

- designing or building bottom sheets components
- reviewing UX/UI for bottom sheets
- implementing interaction pattern for bottom sheets
- your thumb can't reach that menu

## Key Insights & Principles

- Screens keep getting taller while thumbs stay the same length, turning the top of the display into adead zonefor one-handed use.
- Anchor menus and actions to the bottom of the screen, where the thumb naturally rests, instead of the top-right corner most navs default to.
- Unlike a full modal that blocks everything, a bottom sheet keeps the underlying pagevisibleso users never lose their place.
- Addsnap pointsso the sheet can rest half-open or expand to full height, matching how much content the user actually needs.
- Supportdrag-to-dismiss— a downward gesture maps to the sheet's direction and needs no tiny close target to hit.
- Dim the background with ascrimand lock body scroll so only the sheet moves, keeping focus on the active task.

## Do's and Don'ts

- **Do:** Place primary actions within thumb reach at the bottom of the screen
- **Do:** Keep the page visible behind the sheet to preserve context
- **Do:** Offer snap points and drag-to-dismiss for flexible, gesture-friendly height
- **Don't:** Bury frequent menus in the top-right dead zone on tall phones
- **Don't:** Block the whole screen with a full modal when a sheet would do
- **Don't:** Leave the background scrollable while the sheet is open
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/bottom-sheets.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/bottom-sheets.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/bottom-sheets)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
