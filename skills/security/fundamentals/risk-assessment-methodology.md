---
id: security.fundamentals.risk-assessment-methodology
name: Security Risk Assessment Methodology
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Quantitative and qualitative frameworks for identifying, evaluating, and prioritizing cybersecurity risks.
triggers:
- evaluating security vulnerabilities and calculating risk scores
- presenting security risk trade-offs to engineering leadership
- prioritizing vulnerability remediation schedules (CVSS vs business impact)
tags:
- security
- risk-assessment
- cvss
- governance
priority: medium
dependencies: []
related_skills:
- security.system-hardening.vulnerability-assessment-and-prioritization
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Risk Assessment.md
last_updated: '2026-09-14'
---

# Security Risk Assessment Methodology

> Quantitative and qualitative frameworks for identifying, evaluating, and prioritizing cybersecurity risks.

## When to Use (Triggers)

- evaluating security vulnerabilities and calculating risk scores
- presenting security risk trade-offs to engineering leadership
- prioritizing vulnerability remediation schedules (CVSS vs business impact)

## Key Insights & Principles

- Risk Formula: Risk = Threat × Vulnerability × Asset Impact.
- Qualitative vs. Quantitative: Qualitative matrices (Low/Med/High) provide rapid triage; quantitative metrics (SLE, ALE) quantify financial exposure.
- Treatment Options: Mitigate (remediate), Transfer (cyber insurance), Accept (business decision), Avoid (decommission).

## Do's and Don'ts

- **Do:** Pair CVSS technical vulnerability scores with business asset criticality to calculate true risk.
- **Do:** Document every accepted risk with executive sign-off and an expiration review date.
- **Do:** Continuously update risk assessments when system architectures or threat landscapes change.
- **Don't:** Treat CVSS base score in isolation without considering network exposure and compensating controls.
- **Don't:** Leave identified vulnerabilities unaddressed without an explicit documented treatment decision.

## Related Skills

- `security.system-hardening.vulnerability-assessment-and-prioritization`
