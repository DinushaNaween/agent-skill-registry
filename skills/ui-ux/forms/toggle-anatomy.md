---
id: ui-ux.forms.toggle-anatomy
name: Toggle Anatomy
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Two toggles. One snaps. One morphs, and the difference is everything.
triggers:
- designing or building toggle anatomy components
- reviewing UX/UI for toggle anatomy
- implementing forms pattern for toggle anatomy
- two toggles
tags:
- ui
- ux
- forms
- toggle
- anatomy
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.autosave-ux
- ui-ux.forms.date-pickers
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Toggle Anatomy

> Two toggles. One snaps. One morphs, and the difference is everything.

## When to Use (Triggers)

- designing or building toggle anatomy components
- reviewing UX/UI for toggle anatomy
- implementing forms pattern for toggle anatomy
- two toggles

## Key Insights & Principles

- Proportionshold the shape together: make the rail twice the knob's diameter, and pad the knob by its own radius so it sits centered in both states.
- A good togglemorphs, it doesn't snap— animate the flip over ~250ms with an ease-out curve instead of jumping instantly between on and off.
- Four properties change at onceduring the flip: rail color, knob position (translateX), knob shadow, and the state label — all moving together, not in sequence.
- Build inaccessibility: Space toggles the control when focused, a visible focus ring shows keyboard position, and aria-checked lets screen readers announce the state.
- For async toggles, gooptimistic— flip immediately on click, spin a loader inside the knob while the request is pending, then roll back (with a shake and an error toast) if the server fails.

## Do's and Don'ts

- **Do:** Morph rail color, knob position, shadow, and label together over ~250ms with an ease-out curve.
- **Do:** Flip optimistically, show a spinner inside the knob while pending, and roll back on failure.
- **Do:** Support Space to toggle, a visible focus ring, and aria-checked for screen readers.
- **Don't:** Snap the knob instantly between states — the hard jump reads as broken, not responsive.
- **Don't:** Leave the toggle ambiguous during a network request — an un-spun switch looks stuck.
- **Don't:** Ship a toggle that only responds to a mouse click and skips keyboard and screen-reader users.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.autosave-ux`
- `ui-ux.forms.date-pickers`
