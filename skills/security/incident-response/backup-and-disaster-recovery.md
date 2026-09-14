---
id: security.incident-response.backup-and-disaster-recovery
name: Backup Strategies & Disaster Recovery (DR)
version: 1.0.0
domain: security
subdomain: incident-response
summary: The 3-2-1 backup rule, immutable backups against ransomware, and RPO/RTO engineering metrics.
triggers:
- designing enterprise backup and disaster recovery architecture
- defending against ransomware data destruction scenarios
- establishing Recovery Point Objective (RPO) and Recovery Time Objective (RTO)
tags:
- security
- backup
- disaster-recovery
- ransomware
- rpo
- rto
priority: high
dependencies: []
related_skills:
- security.fundamentals.cia-triad
- security.incident-response.incident-response-lifecycle
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: 1-fundamentals/1.2.3.3-Backup-and-disaster-recovery-planning.md
last_updated: '2026-09-14'
---

# Backup Strategies & Disaster Recovery (DR)

> The 3-2-1 backup rule, immutable backups against ransomware, and RPO/RTO engineering metrics.

## When to Use (Triggers)

- designing enterprise backup and disaster recovery architecture
- defending against ransomware data destruction scenarios
- establishing Recovery Point Objective (RPO) and Recovery Time Objective (RTO)

## Key Insights & Principles

- 3-2-1 Rule: 3 copies of data, across 2 different media types, with 1 copy stored offsite/offline.
- Immutable Backups: Write-Once-Read-Many (WORM) storage prevents ransomware operators from deleting backups even with compromised admin credentials.
- RPO (Recovery Point Objective): Maximum acceptable data loss duration (e.g. 15 minutes of transactions).
- RTO (Recovery Time Objective): Maximum acceptable downtime before service restoration (e.g. 2 hours).

## Do's and Don'ts

- **Do:** Enforce air-gapped or immutable cloud backup policies (e.g. AWS S3 Object Lock in Compliance Mode).
- **Do:** Separate backup infrastructure credentials from general production administrative domains.
- **Do:** Schedule automated disaster recovery drill simulations at least quarterly.
- **Don't:** Store backup storage credentials on the same servers being backed up.
- **Don't:** Assume backups are working without regular test restores and checksum validations.

## Practical Implementation & Architecture

Practical implementation of these concepts involves various tools and techniques depending on specific requirements, technology stacks, and organizational constraints. Security professionals should maintain familiarity with industry-standard tools while remaining adaptable to emerging technologies and methodologies.

## Related Skills

- `security.fundamentals.cia-triad`
- `security.incident-response.incident-response-lifecycle`
