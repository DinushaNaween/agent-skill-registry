---
id: security.cryptography.digital-signatures-and-pki
name: Digital Signatures & Public Key Infrastructure (PKI)
version: 1.0.0
domain: security
subdomain: cryptography
summary: Non-repudiation, X.509 certificate validation, Certificate Authorities, and certificate pinning.
triggers:
- configuring TLS/SSL certificates and automated renewal (Let's Encrypt)
- implementing digital document or code signing
- enforcing mutual TLS (mTLS) for microservices
tags:
- security
- pki
- digital-signatures
- certificates
- tls
- x509
priority: medium
dependencies: []
related_skills:
- security.cryptography.symmetric-vs-asymmetric-encryption
- security.network-security.network-security-monitoring
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: 1-fundamentals/1.2.2.2-Digital-signatures-and-certificate-authorities.md
last_updated: '2026-09-14'
---

# Digital Signatures & Public Key Infrastructure (PKI)

> Non-repudiation, X.509 certificate validation, Certificate Authorities, and certificate pinning.

## When to Use (Triggers)

- configuring TLS/SSL certificates and automated renewal (Let's Encrypt)
- implementing digital document or code signing
- enforcing mutual TLS (mTLS) for microservices

## Key Insights & Principles

- Digital Signatures provide authentication, data integrity, and non-repudiation (sender cannot deny creating message).
- PKI Hierarchy: Root CAs sign Intermediate CAs, which sign End-Entity (server/client) certificates.
- Certificate Revocation: CRLs (Certificate Revocation Lists) and OCSP (Online Certificate Status Protocol) monitor revoked certs.
- mTLS: Both client and server present X.509 certificates, authenticating identity in both directions.

## Do's and Don'ts

- **Do:** Automate certificate provisioning and renewals using ACME (Let's Encrypt, Cert-Manager) to prevent expiry outages.
- **Do:** Use ECDSA or Ed25519 for modern digital signatures.
- **Do:** Implement mTLS for all inter-service communications in containerized and Kubernetes environments.
- **Don't:** Disable certificate chain verification (`verify=False` or insecure flags) in production code.
- **Don't:** Expose internal root CA private keys on internet-facing servers.

## Practical Implementation & Architecture

Practical implementation of these concepts involves various tools and techniques depending on specific requirements, technology stacks, and organizational constraints. Security professionals should maintain familiarity with industry-standard tools while remaining adaptable to emerging technologies and methodologies.

## Related Skills

- `security.cryptography.symmetric-vs-asymmetric-encryption`
- `security.network-security.network-security-monitoring`
