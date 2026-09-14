---
id: ui-ux.forms.autosave-ux
name: Autosave
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Saved. It wasn't. Your wifi died mid-word.
triggers:
- designing or building autosave components
- reviewing UX/UI for autosave
- implementing forms pattern for autosave
- saved
tags:
- ui
- ux
- forms
- autosave
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.date-pickers
- ui-ux.forms.form-field-states
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/autosave-ux
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-26'
---

# Autosave

> Saved. It wasn't. Your wifi died mid-word.

## When to Use (Triggers)

- designing or building autosave components
- reviewing UX/UI for autosave
- implementing forms pattern for autosave
- saved

## Key Insights & Principles

- Never write on every keystroke. Start adebounce timerwhen typing pauses, reset it on each key, and commit one clean write after roughly 800ms of silence.
- Model the status indicator as astate machinewith clear states: typing, saving, saved, offline, error. Users trust the pill more than the feature itself, so never let it read 'Saved' when the write never landed.
- When the connection drops, push every edit into alocal queueand surface a badge counting what is pending. On reconnect, drain the queue in order, oldest first.
- Two tabs on one document meanslast write winscan silently erase an hour of someone's work. Merge concurrent changes or warn the user, but never overwrite in silence.
- Guard the exit. If unsaved work exists, use the browser'sbeforeunloadprompt to intercept the closing tab. One ugly dialog beats an afternoon retyped.

## Do's and Don'ts

- **Do:** Debounce writes so one clean save fires after a pause (around 800ms), not on every keystroke.
- **Do:** Queue edits locally while offline and replay them oldest first once the connection returns.
- **Do:** Keep the status honest by mapping it to explicit states and updating it in real time.
- **Don't:** Let the pill show 'Saved' when the change never reached the server.
- **Don't:** Overwrite a concurrent edit silently; merge the changes or warn instead.
- **Don't:** Let a tab close on unsaved work without a confirmation dialog.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/autosave-ux.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/autosave-ux.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/autosave-ux)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.date-pickers`
- `ui-ux.forms.form-field-states`
