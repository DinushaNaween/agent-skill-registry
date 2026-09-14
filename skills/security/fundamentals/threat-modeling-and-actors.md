---
id: security.fundamentals.threat-modeling-and-actors
name: Threat Modeling & Actor Profiling
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Systematic identification of threat actors, capabilities, attack vectors, and high-value targets.
triggers:
- conducting threat modeling for architecture design (STRIDE)
- evaluating adversary motivation (nation-state, cybercrime, insider)
- identifying critical digital assets and attack surface vectors
tags:
- security
- threat-modeling
- stride
- threat-actors
priority: medium
dependencies: []
related_skills:
- security.fundamentals.risk-assessment-methodology
- security.fundamentals.zero-trust-architecture
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Threat Actors.md
last_updated: '2026-09-14'
---

# Threat Modeling & Actor Profiling

> Systematic identification of threat actors, capabilities, attack vectors, and high-value targets.

## When to Use (Triggers)

- conducting threat modeling for architecture design (STRIDE)
- evaluating adversary motivation (nation-state, cybercrime, insider)
- identifying critical digital assets and attack surface vectors

## Key Insights & Principles

- Actor Archetypes: Nation-state APTs (persistence/espionage), Cybercrime Syndicates (financial/ransomware), Hacktivists (reputation), Insider Threats (privileged access).
- STRIDE Model: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
- Crown Jewels Analysis: Protect core databases, key vaults, and intellectual property with disproportionate rigor.

## Do's and Don'ts

- **Do:** Apply STRIDE threat modeling at the design phase before writing application code.
- **Do:** Differentiate defenses based on realistic threat actor capabilities rather than generic checklists.
- **Do:** Include insider threat detection (e.g. unusual data downloads, off-hours access) in monitoring.
- **Don't:** Treat all assets as equally valuable—prioritize defense around identified critical data.
- **Don't:** Assume external hackers are the only threat; unmonitored privileged insiders cause devastating leaks.

## Related Skills

- `security.fundamentals.risk-assessment-methodology`
- `security.fundamentals.zero-trust-architecture`
