# AI Agent Skill Registry

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Skills Catalog](https://img.shields.io/badge/Skills-102%20Indexed%20Skills-success.svg)](./skills)
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

## 📂 Domain Taxonomy & Catalog (102 Skills)

The registry currently houses **102 canonical skills** across two primary software engineering domains:

### 🛡️ Cybersecurity Domain (`skills/security/` - 26 Skills)
| Subdomain | Count | Core Topics & Capabilities |
|---|---|---|
| `fundamentals` | **7** | `Zero Trust Architecture`, `Defense in Depth`, `CIA Triad`, `Cyber Kill Chain`, `MITRE ATT&CK`, `Risk Assessment`, `Threat Actors` |
| `cryptography` | **3** | `Symmetric vs Asymmetric Encryption`, `Hashing & Integrity (SHA-256/Argon2)`, `Digital Signatures & PKI` |
| `access-control` | **2** | `Access Control Models (DAC, MAC, RBAC, ABAC)`, `OS Privilege Management & Sudoers` |
| `network-security` | **2** | `Network Security & Traffic Monitoring`, `DDoS Mitigation Architecture` |
| `app-security` | **3** | `OWASP Top 10 Defenses`, `SQL Injection Prevention`, `API Security & Token Protection` |
| `cloud-security` | **1** | `Cloud Security Posture & IAM Hardening` |
| `system-hardening` | **2** | `System Hardening Baseline (CIS Benchmarks)`, `Vulnerability Assessment & Prioritization` |
| `incident-response` | **3** | `Incident Response Lifecycle (NIST/SANS)`, `Backup & Disaster Recovery (3-2-1 Rule)`, `Bug Bounty & Responsible Disclosure` |
| `ai-security` | **3** | `Adversarial ML & LLM Security (Prompt Injection)`, `AI in Threat Detection`, `AI-Powered SOAR` |

### 🎨 UI/UX Design Domain (`skills/ui-ux/` - 76 Skills)
| Subdomain | Count | Core Topics & Capabilities |
|---|---|---|
| `interaction` | **23** | `CSS :has Selector`, `Context Menus`, `Destructive Actions`, `Bulk Actions`, `Bottom Sheets`, `Drag & Drop`, `Inline Editing`, `Command Palette` |
| `visual` | **20** | `Dark Mode`, `Visual Hierarchy`, `Reverse-Engineered Linear`, `De-AI Landing Hero`, `Shadow Elevation`, `Grid System`, `Depth Layers` |
| `forms` | **12** | `Autosave UX`, `Settings System`, `Password Field UX`, `Date Pickers`, `Stepper Wizard`, `OTP Input`, `Validation Timing` |
| `feedback` | **9** | `Toast Notifications`, `Loading States System`, `Optimistic UI`, `Error States`, `Doherty Threshold`, `Skeleton Loading`, `Undo UX` |
| `content` | **4** | `Empty States`, `Microcopy`, `Landing Page Skeleton`, `Serial Position Effect` |
| `motion` | **4** | `Animation Timing`, `Easing Curves`, `Card Hover Anatomy`, `Scroll-Driven Animations` |
| `navigation` | **4** | `Focus States`, `Navigation Patterns`, `Tabs System`, `Pagination` |

Explore the full interactive markdown map in [`registry.md`](./registry.md) or the JSON index in [`registry.json`](./registry.json).

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
python main.py search "zero trust"
python main.py search "sql injection"
python main.py search "prompt injection"
python main.py search "modal" --domain ui-ux

# Inspect a skill's full markdown content
python main.py load security.fundamentals.zero-trust-architecture
python main.py load ui-ux.interaction.css-has-selector

# Validate all skill files against Schema v1.0
python main.py validate
```

---

## 📑 Skill Schema Specification (v1.0)

Every skill document in `skills/<domain>/<subdomain>/<slug>.md` is self-contained with strict YAML frontmatter:

```markdown
---
id: security.fundamentals.zero-trust-architecture
name: Zero Trust Architecture
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Never trust, always verify: identity-based micro-segmented security architecture.
triggers:
  - designing cloud or enterprise network architecture
  - implementing identity and access management (IAM) or MFA
tags:
  - security
  - zero-trust
  - architecture
priority: high
dependencies: []
related_skills:
  - security.fundamentals.defense-in-depth
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
---

# Zero Trust Architecture

> Never trust, always verify: identity-based micro-segmented security architecture.

## When to Use (Triggers)
- designing cloud or enterprise network architecture
- implementing identity and access management (IAM) or MFA

## Key Insights & Principles
- Never Trust, Always Verify: eliminate traditional perimeter trust.
- Continuous identity and health verification on every request.

## Do's and Don'ts
- **Do:** Require continuous authentication and context verification on every API call.
- **Don't:** Rely on internal network firewalls or VPNs as the sole boundary of trust.
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
