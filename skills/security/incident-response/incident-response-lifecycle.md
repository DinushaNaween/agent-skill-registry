---
id: security.incident-response.incident-response-lifecycle
name: Incident Response Lifecycle (NIST / SANS)
version: 1.0.0
domain: security
subdomain: incident-response
summary: '6-phase incident response methodology: Preparation, Identification, Containment, Eradication, Recovery, and Lessons
  Learned.'
triggers:
- handling an active security incident or breach alert
- authoring incident response runbooks and escalation trees
- conducting post-incident reviews (blameless post-mortems)
tags:
- security
- incident-response
- nist
- sans
- forensics
priority: high
dependencies: []
related_skills:
- security.incident-response.backup-and-disaster-recovery
- security.fundamentals.cyber-kill-chain
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/9. Incident Response & Reporting/9. Incident Response & Reporting.md
last_updated: '2026-09-14'
---

# Incident Response Lifecycle (NIST / SANS)

> 6-phase incident response methodology: Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned.

## When to Use (Triggers)

- handling an active security incident or breach alert
- authoring incident response runbooks and escalation trees
- conducting post-incident reviews (blameless post-mortems)

## Key Insights & Principles

- Phase 1: Preparation (tools, jumpboxes, communications out-of-band, access policies).
- Phase 2: Identification (triage alerts, confirm true positive, establish scope of breach).
- Phase 3: Containment (short-term network isolation vs long-term system segmentation while preserving forensic evidence).
- Phase 4: Eradication (clean malware, rotate compromised credentials, patch root-cause vulnerabilities).
- Phase 5: Recovery (re-introduce systems with heightened monitoring, test business functions).
- Phase 6: Lessons Learned (document timeline, identify defensive gaps, update runbooks within 2 weeks).

## Do's and Don'ts

- **Do:** Isolate compromised machines from the network without powering off immediately to preserve volatile RAM evidence.
- **Do:** Establish out-of-band communication channels (Signal, phone) in case email/Slack is compromised.
- **Do:** Conduct blameless post-mortems and track remediation action items to completion.
- **Don't:** Power off or reboot an infected machine immediately—this destroys critical volatile memory forensic artifacts.
- **Don't:** Declare an incident resolved before verifying eradication and rotating all potentially exposed secrets.

## Related Skills

- `security.incident-response.backup-and-disaster-recovery`
- `security.fundamentals.cyber-kill-chain`
