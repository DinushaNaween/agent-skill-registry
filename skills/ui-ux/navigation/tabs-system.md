---
id: ui-ux.navigation.tabs-system
name: Tabs System
version: 1.0.0
domain: ui-ux
subdomain: navigation
summary: Tabs aren't a widget. They're a system. Stop letting them jump.
triggers:
- designing or building tabs system components
- reviewing UX/UI for tabs system
- implementing navigation pattern for tabs system
- tabs aren't a widget
tags:
- ui
- ux
- navigation
- tabs
- system
priority: medium
dependencies: []
related_skills:
- ui-ux.navigation.navigation-patterns
- ui-ux.navigation.focus-states
- ui-ux.navigation.pagination
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Tabs System

> Tabs aren't a widget. They're a system. Stop letting them jump.

## When to Use (Triggers)

- designing or building tabs system components
- reviewing UX/UI for tabs system
- implementing navigation pattern for tabs system
- tabs aren't a widget

## Key Insights & Principles

- Theactive indicatorshould slide, never teleport. Drive it with a spring and match its timing to the content fade —slow in, fast out.
- When tabs overflow one screen, neverwrap to a second line. Scroll horizontally, addedge fadesto hint at what's off-screen, and put chevron buttons on desktop.
- Make it keyboard-operable:arrowsmove between tabs,Homejumps to first,Endto last, andTabexits to the next focusable group.
- Thefocus ring and the active state must never share a color— otherwise keyboard users can't tell where they are versus what's selected.
- Content should never hard-cut on switch.Fade out, pause ~80ms, fade in, and match panel heights so nothing shifts.
- Mobile isn't a shrunk desktop: use asegmented control under 5 tabs, abottom sheet over 5, never a scaled-down bar.

## Do's and Don'ts

- **Do:** Slide the active indicator with a spring, timed to match the content fade
- **Do:** Scroll an overflowing tab row horizontally with edge fades and desktop chevrons
- **Do:** Give the focus ring and active state distinct colors
- **Don't:** Wrap an overflowing tab row onto a second line
- **Don't:** Hard-cut content on switch — fade out, pause, fade in instead
- **Don't:** Reuse the desktop tab bar shrunk down on mobile
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.navigation.navigation-patterns`
- `ui-ux.navigation.focus-states`
- `ui-ux.navigation.pagination`
