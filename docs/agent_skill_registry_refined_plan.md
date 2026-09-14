# Refined Plan: Hierarchical AI Agent Skill Registry & Automated Knowledge Ingestion

## 1. Executive Summary

This document refines and expands upon the original [Agent Skill Registry Architectural Plan](./agent_skill_registry_architectural_plan.md). 

The goal is to build an **extensible, machine-discoverable, human-readable Agent Skill Registry** across all core software engineering domains, coupled with an **automated Ingestion & Harvester Engine** capable of extracting patterns, best practices, and actionable rules from public engineering resources and compiling them into canonical skill documents.

---

## 2. Core Vision: The Self-Growing Agent Skill Registry

```text
       External Knowledge Sources
 (Web Standards, OWASP, Refactoring Catalogs, Docs)
                     │
                     ▼
          ┌─────────────────────┐
          │   Harvester Layer   │  (Pluggable site adapters,
          │  (Scraper & Parser) │   rate-limiting, normalization)
          └──────────┬──────────┘
                     │ Normalized Skill Objects
                     ▼
          ┌─────────────────────┐
          │  Ingestion & Merge  │  (Schema validation, hashing,
          │       Engine        │   idempotent updates, indexing)
          └──────────┬──────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   Agent Skill Registry  │
        │   (Filesystem + JSON)   │
        ├─────────────────────────┤
        │  • registry.md          │ <── Lightweight Map for Agents & Humans
        │  • registry.json        │ <── Machine-Readable Index & Search
        │  • skills/<domain>/...  │ <── Canonical Markdown Skill Units
        └────────────┬────────────┘
                     │
          Discovery & Context Injection
                     │
                     ▼
         ┌───────────────────────┐
         │       AI Agent        │
         │  (Claude, Gemini, etc)│
         └───────────────────────┘
```

---

## 3. Standardized Skill Specification (v1.0)

Every skill in the registry adheres to a strict schema with YAML frontmatter. This ensures AI agents can parse metadata, evaluate activation criteria, and resolve dependencies without reading the full body text.

### 3.1 YAML Frontmatter Schema

```yaml
---
id: ui-ux.interaction.accordion-disclosure
name: Accordion Disclosure
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: One accordion glides open, the other jumps. Four small rules separate them.
triggers:
  - designing accordion or collapsible sections
  - expanding or disclosing content dynamically
  - handling multiple vs single open accordion panels
  - accessible disclosures and aria-expanded
tags:
  - ui
  - ux
  - interaction
  - accordion
  - animation
  - accessibility
priority: medium
dependencies: []
related_skills:
  - ui-ux.motion.animation-timing
  - ui-ux.interaction.focus-states
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: "2026-09-14"
---
```

### 3.2 Standard Skill Document Sections

1. **`# [Skill Name]`**: Clear title and one-line summary hook.
2. **`## When to Use (Triggers)`**: Explicit scenarios where the agent must load this skill.
3. **`## Key Principles & Insights`**: Foundational rules, state considerations, rationale.
4. **`## Do's & Don'ts`**: Crisp, binary dos and don'ts formatted as actionable bullet points.
5. **`## Code & Implementation Snippets`**: Copy-pasteable, production-ready code (CSS selectors, HTML semantics, JS handlers, backend patterns).
6. **`## References`**: Cross-links to standards and complementary documentation.

---

## 4. Domain Taxonomy & Directory Organization

```text
skills/
├── ui-ux/                                       # UI/UX design patterns
│   ├── interaction/
│   ├── visual/
│   ├── forms/
│   ├── motion/
│   ├── content/
│   ├── feedback/
│   └── navigation/
├── security/                                    # Security best practices & hardening
│   ├── fundamentals/
│   ├── cryptography/
│   ├── access-control/
│   ├── network-security/
│   ├── app-security/
│   ├── cloud-security/
│   ├── system-hardening/
│   ├── incident-response/
│   └── ai-security/
├── architecture/                                # Future: Clean arch & API design
├── dotnet/                                      # Future: .NET / C# best practices
├── database/                                    # Future: SQL, indexing, optimization
└── testing/                                     # Future: Unit, integration, E2E
```

---

## 5. Agent Discovery & Consumption Lifecycle

When an AI agent is executing a user request, it discovers and consumes skills using a 5-step lifecycle:

```text
Step 1: Task Analysis
Agent analyzes prompt: "Build a responsive modal dialog with animated backdrop and scroll locking."

Step 2: Capability Query (Lightweight)
Agent queries registry.json or scans registry.md triggers:
Matches:
- ui-ux.interaction.modal-hierarchy
- ui-ux.interaction.css-has-selector
- ui-ux.motion.animation-timing

Step 3: Dependency Resolution
Agent inspects dependencies in frontmatter.

Step 4: Selective Loading
Agent loads ONLY the matched markdown files into its working context (saving tokens).

Step 5: Execution & Verification
Agent applies the specific dos/don'ts and code patterns to generate production-standard code.
```
