---
id: ui-ux.interaction.context-menu
name: Context Menu
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: A context menu is a system, not just a list of actions.
triggers:
- designing or building context menu components
- reviewing UX/UI for context menu
- implementing interaction pattern for context menu
- a context menu is a system, not just a list of actions
tags:
- ui
- ux
- interaction
- context
- menu
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-14'
---

# Context Menu

> A context menu is a system, not just a list of actions.

## When to Use (Triggers)

- designing or building context menu components
- reviewing UX/UI for context menu
- implementing interaction pattern for context menu
- a context menu is a system, not just a list of actions

## Key Insights & Principles

- A context menumeasures before it opens. No room below, it flips up; no room to the right, it mirrors left, always anchored to your cursor and always inside the viewport.
- Twelve flat actions read as noise.Group by intentand split with dividers: pair Rename with Duplicate, Share with Copy link, and isolateDelete at the bottom in red.
- Submenus die the instant the cursor drifts off the row. Draw aninvisible safe trianglefrom cursor to submenu so the menu holds while you move diagonally toward it. That is hover intent.
- Power users never aim.Arrowswalk the list,letters jump(press D, land on Duplicate), andEscapecloses one level, not the whole menu.
- Mobile has no right click. Along pressopens the same actions as abottom sheet: one menu system, two triggers.

## Do's and Don'ts

- **Do:** Measure available space and flip the menu so it always opens inside the viewport.
- **Do:** Group actions by intent with dividers, and set the destructive action apart at the bottom in red.
- **Do:** Add a safe triangle from cursor to submenu so it survives a diagonal move.
- **Don't:** Close a submenu the moment the cursor leaves the row, ignoring the diagonal path toward it.
- **Don't:** Dump a dozen ungrouped actions into one flat, unscannable list.
- **Don't:** Ship right-click only; wire a long press to the same actions on mobile.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
