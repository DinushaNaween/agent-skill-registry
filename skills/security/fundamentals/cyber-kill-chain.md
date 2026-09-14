---
id: security.fundamentals.cyber-kill-chain
name: Cyber Kill Chain & Attack Lifecycle
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Lockheed Martin 7-phase cyberattack lifecycle model and defensive intervention techniques.
triggers:
- analyzing an ongoing or simulated security intrusion
- designing detection rules and early warning alert triggers
- modeling threat actor advancement through internal networks
tags:
- security
- kill-chain
- threat-intelligence
- incident-response
priority: medium
dependencies: []
related_skills:
- security.fundamentals.mitre-attck-framework
- security.incident-response.incident-response-lifecycle
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Cyber Kill Chain.md
last_updated: '2026-09-14'
---

# Cyber Kill Chain & Attack Lifecycle

> Lockheed Martin 7-phase cyberattack lifecycle model and defensive intervention techniques.

## When to Use (Triggers)

- analyzing an ongoing or simulated security intrusion
- designing detection rules and early warning alert triggers
- modeling threat actor advancement through internal networks

## Key Insights & Principles

- The 7 Phases: Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control (C2) → Actions on Objectives.
- Early Interruption: Breaking any single link in the kill chain halts the entire attack progression.
- Dwell Time Reduction: Detecting attackers during delivery or exploitation prevents destructive impact on objectives.

## Do's and Don'ts

- **Do:** Deploy threat intelligence feeds and DNS filtering to detect weaponized C2 infrastructure early.
- **Do:** Implement email filtering and endpoint execution restrictions to neutralize Delivery and Exploitation.
- **Do:** Monitor egress traffic for beaconing patterns to catch Command & Control communication.
- **Don't:** Wait until the 'Actions on Objectives' phase (e.g. data exfiltration or ransomware) before triggering alerts.
- **Don't:** Ignore external reconnaissance indicators such as aggressive port scanning and OSINT scraping.

## Related Skills

- `security.fundamentals.mitre-attck-framework`
- `security.incident-response.incident-response-lifecycle`
