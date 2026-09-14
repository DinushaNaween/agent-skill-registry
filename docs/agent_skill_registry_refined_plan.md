# Refined Plan: Hierarchical AI Agent Skill Registry & Automated Knowledge Harvester

## 1. Executive Summary

This document refines and expands upon the original [Agent Skill Registry Architectural Plan](./agent_skill_registry_architectural_plan.md). 

The goal is to build an **extensible, machine-discoverable, human-readable Agent Skill Registry** across all core software engineering domains, coupled with an **automated Harvester / Scraper Engine** capable of extracting patterns, best practices, and actionable rules from external websites (starting with [designmotionhq.com/patterns](https://www.designmotionhq.com/patterns)) and compiling them into canonical skill documents.

---

## 2. Core Vision: The Self-Growing Agent Skill Registry

```text
       External Knowledge Sources
  (DesignMotionHQ, OWASP, Refactoring.Guru, Docs)
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
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/accordion-disclosure
  media:
    thumbnail: https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/accordion-disclosure.jpg
    video: https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/accordion-disclosure.mp4
last_updated: "2026-09-14"
---
```

### 3.2 Standard Skill Document Sections

1. **`# [Skill Name]`**: Clear title and one-line summary hook.
2. **`## When to Use (Triggers)`**: Explicit scenarios where the agent must load this skill.
3. **`## Key Principles & Insights`**: Foundational rules, DOM/state considerations, UX rationale.
4. **`## Do's & Don'ts`**: Crisp, binary dos and don'ts formatted as actionable bullet points.
5. **`## Code & Implementation Snippets`**: Copy-pasteable, production-ready code (CSS selectors, HTML semantics, JS handlers, C# patterns, etc.).
6. **`## Visual References & Demos`**: Direct links to video breakdowns and visual thumbnails.
7. **`## Related Skills & Dependencies`**: Cross-links to complementary skills.

---

## 4. Pluggable Harvester & Scraper Pipeline

To support ingesting skills from any similar technical or design repository, the scraping engine is structured around an extensible **Adapter Pattern**:

```text
              BaseHarvester (Abstract Interface)
               ├── discover() -> List[str]
               ├── extract(url) -> RawPageData
               └── normalize(RawPageData) -> Skill
                            ▲
            ┌───────────────┴───────────────┐
            │                               │
  DesignMotionHQHarvester          GenericHtmlHarvester
  (Extracts 76 UI/UX patterns,    (Heuristic-based scraper for
   Next.js metadata, video/mp4,    markdown blogs, documentation,
   insights & dos/donts)           and pattern repositories)
```

### Pipeline Steps:
1. **Discover**: Crawls index or sitemap to discover all pattern/skill URLs.
2. **Extract**: Downloads raw HTML/JSON with retry logic and polite rate limiting (0.5s–1.0s).
3. **Normalize**: Maps scraped content into the canonical `Skill` data model.
4. **Ingest & Merge**:
   - Checks content hash: skips unchanged skills unless `--force` is set.
   - Writes or updates individual markdown skill files in `skills/<domain>/<subdomain>/<slug>.md`.
   - Re-indexes the entire registry into `registry.md` and `registry.json`.

---

## 5. Domain Taxonomy & Directory Organization

```text
Web-Scraper/
├── docs/
│   ├── agent_skill_registry_architectural_plan.md  # Original base plan
│   └── agent_skill_registry_refined_plan.md        # This document
├── registry.md                                      # Human & Agent readable map of all skills
├── registry.json                                    # Structured metadata index
├── skills/                                          # Canonical skills tree
│   ├── ui-ux/                                       # Populated by DesignMotionHQ harvester
│   │   ├── interaction/
│   │   ├── visual/
│   │   ├── forms/
│   │   ├── motion/
│   │   ├── content/
│   │   ├── feedback/
│   │   └── navigation/
│   ├── security/                                    # Future: OWASP & secure coding
│   ├── architecture/                                # Future: Clean arch & API design
│   ├── dotnet/                                      # Future: .NET / C# best practices
│   ├── database/                                    # Future: SQL, indexing, optimization
│   └── testing/                                     # Future: Unit, integration, E2E
├── harvesters/                                      # Extensible scraper adapters
│   ├── __init__.py
│   ├── base.py                                      # Abstract BaseHarvester
│   ├── models.py                                    # Dataclasses: Skill, Media, Source
│   ├── designmotionhq.py                            # Production DesignMotionHQ adapter
│   └── generic.py                                   # Configurable generic adapter
├── registry_engine/                                 # Ingestion & indexer engine
│   ├── __init__.py
│   ├── writer.py                                    # Markdown skill serializer with YAML
│   ├── indexer.py                                   # Generates registry.md and registry.json
│   └── search.py                                    # CLI/API skill search & discovery
├── main.py                                          # Master CLI interface
└── requirements.txt
```

---

## 6. Agent Discovery & Consumption Lifecycle

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
Agent inspects dependencies in frontmatter (none required or loads prerequisite skills).

Step 4: Selective Loading
Agent loads ONLY the 3 matched markdown files into its working context (saving tokens).

Step 5: Execution & Verification
Agent applies the specific dos/don'ts and CSS/JS patterns to generate high-standard code.
```

---

## 7. Next Steps & Implementation Roadmap

1. **Phase 1: Foundation & Core Harvester Engine**
   - Implement `harvesters/models.py` and `harvesters/base.py`.
   - Implement `harvesters/designmotionhq.py` to extract all 76 UI/UX patterns.
   - Implement `registry_engine/writer.py` to output canonical skills.
   - Implement `registry_engine/indexer.py` to generate `registry.md` and `registry.json`.

2. **Phase 2: Execution & Verification on DesignMotionHQ**
   - Run scraper on `https://www.designmotionhq.com/patterns`.
   - Verify extraction of 76 skills across `ui-ux/*`.
   - Validate YAML frontmatter, media links, insights, and dos/donts.

3. **Phase 3: Generic Adapter & CLI Tooling**
   - Add discovery CLI: `python main.py search <keyword>` and `python main.py load <skill_id>`.
   - Add extensible harvester CLI: `python main.py harvest --source designmotionhq` or `--source generic --url <url>`.
