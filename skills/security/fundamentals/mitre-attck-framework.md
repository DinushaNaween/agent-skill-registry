---
id: security.fundamentals.mitre-attck-framework
name: MITRE ATT&CK Framework Mapping
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Curated knowledge base of cyber adversary tactics, techniques, and procedures (TTPs).
triggers:
- mapping defensive security monitoring to real adversary techniques
- conducting threat modeling and red/blue team simulations
- assessing security coverage gaps across SIEM detection rules
tags:
- security
- mitre
- attck
- threat-detection
- siem
priority: high
dependencies: []
related_skills:
- security.fundamentals.cyber-kill-chain
- security.system-hardening.vulnerability-assessment-and-prioritization
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/MITRE ATT&CK Framework.md
last_updated: '2026-09-14'
---

# MITRE ATT&CK Framework Mapping

> Curated knowledge base of cyber adversary tactics, techniques, and procedures (TTPs).

## When to Use (Triggers)

- mapping defensive security monitoring to real adversary techniques
- conducting threat modeling and red/blue team simulations
- assessing security coverage gaps across SIEM detection rules

## Key Insights & Principles

- Tactics represent the 'why' (e.g. Initial Access, Privilege Escalation, Lateral Movement, Exfiltration).
- Techniques describe 'how' adversaries accomplish the tactic (e.g. T1059 Command and Scripting Interpreter).
- Sub-techniques provide granular specifics (e.g. T1059.001 PowerShell).
- Matrix coverage mapping reveals blind spots where log telemetry is insufficient.

## Do's and Don'ts

- **Do:** Map your SIEM correlation rules and detection alerts directly to ATT&CK Technique IDs.
- **Do:** Prioritize detection rules for techniques commonly used by threat actors targeting your industry.
- **Do:** Simulate adversary techniques using tools like Atomic Red Team to validate alert coverage.
- **Don't:** Assume high logging volume equals security visibility without verified detection rules mapped to TTPs.
- **Don't:** Treat ATT&CK as a checklist to 'score 100%' rather than an adversary-grounded risk model.

## Related Skills

- `security.fundamentals.cyber-kill-chain`
- `security.system-hardening.vulnerability-assessment-and-prioritization`
