---
id: security.cloud-security.cloud-security-fundamentals
name: Cloud Security Posture & IAM Hardening
version: 1.0.0
domain: security
subdomain: cloud-security
summary: Shared Responsibility Model, least-privilege IAM policies, cloud storage security, and CSPM baselines.
triggers:
- architecting cloud infrastructure (AWS, Azure, GCP)
- configuring cloud IAM roles, bucket policies, and security groups
- auditing cloud misconfigurations and public asset exposures
tags:
- security
- cloud
- aws
- azure
- iam
- s3
- cspm
priority: high
dependencies: []
related_skills:
- security.fundamentals.zero-trust-architecture
- security.system-hardening.system-hardening-baseline
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/8. Cloud Security Fundamentals/8. Cloud Security Fundamentals.md
last_updated: '2026-09-14'
---

# Cloud Security Posture & IAM Hardening

> Shared Responsibility Model, least-privilege IAM policies, cloud storage security, and CSPM baselines.

## When to Use (Triggers)

- architecting cloud infrastructure (AWS, Azure, GCP)
- configuring cloud IAM roles, bucket policies, and security groups
- auditing cloud misconfigurations and public asset exposures

## Key Insights & Principles

- Shared Responsibility: Cloud provider secures the cloud (hardware, facilities); customer secures what's in the cloud (data, IAM, network).
- IAM Principle: Never use root accounts for workloads; use temporary STS role credentials instead of long-lived access keys.
- Storage Bucket Security: S3 buckets and Azure blobs must block public access by default, with encryption at rest enabled.
- Cloud Security Posture Management (CSPM): Continuous automated auditing for compliance drift and open security groups.

## Do's and Don'ts

- **Do:** Enforce multi-factor authentication (MFA) on all cloud management console accounts.
- **Do:** Enable cloud audit logging (AWS CloudTrail, Azure Activity Log) with log integrity validation and centralized forwarding.
- **Do:** Use infrastructure-as-code (Terraform, CloudFormation) with automated security linting (Checkov, tfsec).
- **Don't:** Commit cloud access keys (`AKIA...`) or service account JSON files to Git repositories.
- **Don't:** Allow `0.0.0.0/0` inbound rules on security groups for sensitive administrative ports (SSH, RDP, databases).

## Related Skills

- `security.fundamentals.zero-trust-architecture`
- `security.system-hardening.system-hardening-baseline`
