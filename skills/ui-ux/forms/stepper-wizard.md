---
id: ui-ux.forms.stepper-wizard
name: Stepper Wizard
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Twelve fields, one wall. Four steps, one path.
triggers:
- designing or building stepper wizard components
- reviewing UX/UI for stepper wizard
- implementing forms pattern for stepper wizard
- twelve fields, one wall
tags:
- ui
- ux
- forms
- stepper
- wizard
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.autosave-ux
- ui-ux.forms.date-pickers
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/stepper-wizard
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Stepper Wizard

> Twelve fields, one wall. Four steps, one path.

## When to Use (Triggers)

- designing or building stepper wizard components
- reviewing UX/UI for stepper wizard
- implementing forms pattern for stepper wizard
- twelve fields, one wall

## Key Insights & Principles

- Chunklong forms into small groups — three fields read effortlessly, but twelve in a row trigger scroll fatigue. Splitting the flow lowers cognitive load before it breaks it.
- Group fields bycontext, not by count— Personal, Shipping, Payment, Review. Each step should earn its own screen; splits made on an arbitrary number feel random.
- Always showprogress. Pick one indicator — a linear bar, numbered dots, or step labels — so users can feel the end getting close.
- Validate inside each step, not at the end. A bad email on step one shouldn't surface on step four; block the Next button while a field is still invalid.
- Preferinline errorsover final-screen rejection — an immediate red message beats bouncing users all the way back after they thought they were finished.
- Persist stateon every step change. Back navigation and a page refresh must preserve entered data — lose the form once and you lose the user.

## Do's and Don'ts

- **Do:** Split forms into steps grouped by meaning like Personal, Payment or Review, not by an arbitrary field count.
- **Do:** Show a progress indicator and validate each field within its own step.
- **Do:** Save entered data so Back and Refresh never wipe the user's progress.
- **Don't:** Surface a step-one error only once the user reaches the final step.
- **Don't:** Let a refresh or the Back button discard everything already typed.
- **Don't:** Stack twelve fields into one scrolling wall when they can be chunked into steps.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/stepper-wizard.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/stepper-wizard.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/stepper-wizard)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.autosave-ux`
- `ui-ux.forms.date-pickers`
