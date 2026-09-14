# AI Agent Skill Registry

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Skills Catalog](https://img.shields.io/badge/Skills-76%20Indexed%20Skills-success.svg)](./skills)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/DinushaNaween/agent-skill-registry/pulls)

A hierarchical, machine-discoverable knowledge and skill repository designed specifically for autonomous AI agents and software engineers.

Instead of stuffing thousands of lines of documentation or full design systems into an agent's prompt, the **Skill Registry** allows AI agents to dynamically discover, select, and load only the exact engineering skills needed for a given task.

---

## 🎯 Architectural Concept

The central lifecycle is:

$$\text{Task Request} \longrightarrow \text{Registry Query} \longrightarrow \text{Discovery} \longrightarrow \text{Selective Loading} \longrightarrow \text{Execution}$$

```text
                           User / Task Request
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   AI Agent / LLM    │
                        └──────────┬──────────┘
                                   │
                        1. Query registry.json / CLI
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │    Skill Registry Index   │
                     │  (registry.md / .json)    │
                     └─────────────┬─────────────┘
                                   │
                        2. Match triggers & return path
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │   Selective Context Load  │
                     │ (skills/<domain>/<id>.md) │
                     └─────────────┬─────────────┘
                                   │
                        3. Execute task with precision
                                   │
                                   ▼
                           High-Quality Output
```

---

## 📂 Domain Taxonomy & Structure

The repository organizes engineering capabilities into logical domains and subdomains:

```text
skills/
├── ui-ux/                               # UI/UX Design Patterns & Rules
│   ├── content/                         # Empty states, microcopy, etc.
│   ├── feedback/                        # Toasts, error recovery, loading states
│   ├── forms/                           # Autosave, settings, OTP, date pickers
│   ├── interaction/                     # CSS :has, modals, context menus, actions
│   ├── motion/                          # Timing, easing curves, hover anatomy
│   ├── navigation/                      # Command palette, tabs, pagination
│   └── visual/                          # Dark mode, visual hierarchy, tokens
├── security/                            # (In Progress) OWASP, secure coding, auth
├── architecture/                        # (Planned) Clean architecture, API design
├── dotnet/                              # (Planned) C# idioms, ASP.NET Core, EF Core
├── database/                            # (Planned) Indexing, SQL optimization
└── testing/                             # (Planned) Unit, integration, E2E strategies
```

---

## 🚀 Quick Start

### 1. Clone & Set Up

```bash
git clone https://github.com/DinushaNaween/agent-skill-registry.git
cd agent-skill-registry
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Discover & Search Skills

```bash
# List all registered skills across domains
python main.py list

# Search skills by keyword, tag, or trigger
python main.py search "modal"
python main.py search "dark mode"
python main.py search "validation" --domain ui-ux

# Inspect a skill's full markdown content
python main.py load ui-ux.interaction.modal-hierarchy

# Validate all skill files against Schema v1.0
python main.py validate
```

---

## 📑 Skill Schema Specification (v1.0)

Every skill document in `skills/<domain>/<subdomain>/<slug>.md` is self-contained with strict YAML frontmatter:

```markdown
---
id: ui-ux.interaction.accordion-disclosure
name: Accordion Disclosure
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: One accordion glides open, the other jumps. Four small rules separate them.
triggers:
  - designing or building accordion disclosure components
  - reviewing UX/UI for accordion disclosure
tags:
  - ui
  - ux
  - interaction
  - accordion
priority: medium
dependencies: []
related_skills:
  - ui-ux.motion.animation-timing
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/accordion-disclosure
---

# Accordion Disclosure

> One accordion glides open, the other jumps. Four small rules separate them.

## When to Use (Triggers)
- designing or building accordion disclosure components
- reviewing UX/UI for accordion disclosure

## Key Insights & Principles
- Animate height using grid-template-rows: 0fr to 1fr instead of max-height hacks.
- The browser calculates fractional grid rows smoothly; max-height introduces cubic-bezier lag.

## Do's and Don'ts
- **Do:** Use aria-expanded on the trigger button to announce state to assistive tech.
- **Don't:** Hardcode a max-height in pixels that clips unpredictable content.

## Code & Selectors
```css
.accordion-content {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 250ms ease-out;
}
.accordion-item[aria-expanded="true"] .accordion-content {
  grid-template-rows: 1fr;
}
```
```

---

## 🤖 AI Agent Integration Guide

### Option 1: System Prompt / Cursor Rules

Add this directive to your agent's system prompt or `.cursorrules`:

```text
When working on specialized tasks (UI/UX, security, architecture):
1. Search the Skill Registry: `python main.py search "<task keyword>"`
2. Load matching skill: `python main.py load <skill_id>`
3. Strictly follow the Principles, Do's/Don'ts, and Code patterns in the skill.
```

### Option 2: Python / LangChain Tool

```python
import subprocess

def get_skill(skill_id: str) -> str:
    """Retrieve canonical skill instructions by ID."""
    result = subprocess.run(
        ["python", "main.py", "load", skill_id],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout
```

---

## 🤝 Contributing

We welcome skill contributions across all engineering disciplines!
1. Check existing skills in [`registry.md`](./registry.md).
2. Create your skill in `skills/<domain>/<subdomain>/<slug>.md` following Schema v1.0.
3. Run `python main.py validate` to verify schema compliance.
4. Run `python main.py reindex` to update indexes.
5. Submit a pull request!

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.

---

## 👤 Author

**Dinusha Naveen Dasanayaka**
- Senior Software Engineer
- GitHub: [@DinushaNaween](https://github.com/DinushaNaween)
- Email: dldndasanayaka@gmail.com
