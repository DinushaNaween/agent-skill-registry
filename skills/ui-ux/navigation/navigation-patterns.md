---
id: ui-ux.navigation.navigation-patterns
name: Navigation Patterns
version: 1.0.0
domain: ui-ux
subdomain: navigation
summary: 'Five nav patterns, one system: mobile = tabs, desktop = sidebar.'
triggers:
- designing or building navigation patterns components
- reviewing UX/UI for navigation patterns
- implementing navigation pattern for navigation patterns
- 'five nav patterns, one system: mobile = tabs, desktop = sidebar'
tags:
- ui
- ux
- navigation
- patterns
priority: medium
dependencies: []
related_skills:
- ui-ux.navigation.tabs-system
- ui-ux.navigation.focus-states
- ui-ux.navigation.pagination
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Navigation Patterns

> Five nav patterns, one system: mobile = tabs, desktop = sidebar.

## When to Use (Triggers)

- designing or building navigation patterns components
- reviewing UX/UI for navigation patterns
- implementing navigation pattern for navigation patterns
- five nav patterns, one system: mobile = tabs, desktop = sidebar

## Key Insights & Principles

- Bottom tabsare the mobile default: 3-5 top destinations, always visible and within thumb reach. Burying those same links in a hamburger drops engagement ~40%.
- Apersistent sidebaris the desktop answer for hierarchical content with 5+ sections — keep it in view, since collapsing it by default kills discoverability.
- Thehamburgeris secondary navigation, never primary. It's acceptable on mobile, but hiding the menu on desktop drops engagement ~56%.
- Acommand palette(Cmd K) is a search-driven accelerator for power users — pair it with visible nav, because new users don't know it exists.
- Breadcrumbsonly earn their space when the hierarchy runs deeper than 2 levels; on flat structures they add noise instead of orientation.
- Choose byplatform and depth, not taste — the whole set is one system, not five interchangeable options.

## Do's and Don'ts

- **Do:** Match the pattern to the platform: bottom tabs on mobile, a persistent sidebar on desktop.
- **Do:** Keep primary destinations visible — 3-5 for tabs, 5+ sections to justify a sidebar.
- **Do:** Reserve breadcrumbs for hierarchies deeper than two levels.
- **Don't:** Hide primary navigation in a hamburger — engagement drops 40-56%.
- **Don't:** Make a command palette the only path to a feature; new users won't discover it.
- **Don't:** Add breadcrumbs to a flat structure where they're just visual noise.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.navigation.tabs-system`
- `ui-ux.navigation.focus-states`
- `ui-ux.navigation.pagination`
