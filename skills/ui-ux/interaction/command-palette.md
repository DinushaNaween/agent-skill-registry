---
id: ui-ux.interaction.command-palette
name: Command Palette
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: ⌘K is a system, not a search box.
triggers:
- designing or building command palette components
- reviewing UX/UI for command palette
- implementing interaction pattern for command palette
- ⌘k is a system, not a search box
tags:
- ui
- ux
- interaction
- command
- palette
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-08'
---

# Command Palette

> ⌘K is a system, not a search box.

## When to Use (Triggers)

- designing or building command palette components
- reviewing UX/UI for command palette
- implementing interaction pattern for command palette
- ⌘k is a system, not a search box

## Key Insights & Principles

- Usefuzzy matching, not exact substring search — typing "stg" should still surface "Settings", "Storage", and "Staging". Exact matching returns nothing and feels broken.
- Group resultsinto labeled sections (Recent, Actions, Pages) so a long flat list becomes scannable structure instead of an undifferentiated wall.
- Make itfully keyboard-driven: arrows move the highlight, Enter runs the selected command, Esc closes — never force the user back to the mouse.
- Never open to a blank void.Prefill recent or suggested commandsso people have a starting point before they type a single character.
- Forasync commands, show an inline spinner and keep the palette open — load results in place rather than freezing the whole screen.
- Supportnested commands: one command can drill into a sub-menu with a breadcrumb, and Esc walks back exactly one level.

## Do's and Don'ts

- **Do:** Match queries as fuzzy subsequences so "stg" still finds "Settings"
- **Do:** Prefill recent and suggested commands so the palette opens with something to act on
- **Do:** Drive everything from the keyboard — arrows to move, Enter to run, Esc to go back
- **Don't:** Require exact substring matches — "stg" ≠ "Settings" leaves users staring at "No results"
- **Don't:** Open to a blank "No results" void with nothing to select
- **Don't:** Freeze the whole screen while an async command loads instead of spinning inline
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
