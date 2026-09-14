---
id: security.cryptography.hashing-and-integrity
name: Cryptographic Hashing & Data Integrity
version: 1.0.0
domain: security
subdomain: cryptography
summary: Secure hashing with SHA-256/SHA-3, collision attack defenses, and salted password storage with Argon2/bcrypt.
triggers:
- storing user passwords or credentials in a database
- verifying software download integrity or file tampering
- implementing HMAC signatures for API authentication
tags:
- security
- cryptography
- hashing
- passwords
- argon2
- sha256
priority: high
dependencies: []
related_skills:
- security.cryptography.symmetric-vs-asymmetric-encryption
- security.access-control.access-control-models
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: 1-fundamentals/1.2.2.1-Hashing-algorithms-MD5-SHA-256-and-collision-attacks.md
last_updated: '2026-09-14'
---

# Cryptographic Hashing & Data Integrity

> Secure hashing with SHA-256/SHA-3, collision attack defenses, and salted password storage with Argon2/bcrypt.

## When to Use (Triggers)

- storing user passwords or credentials in a database
- verifying software download integrity or file tampering
- implementing HMAC signatures for API authentication

## Key Insights & Principles

- One-Way Function: Deterministic, pre-image resistant, second pre-image resistant, and collision resistant.
- General Hashing (SHA-256, SHA-3, BLAKE3): Designed to be fast; ideal for checksums, HMACs, and digital signatures.
- Password Hashing (Argon2id, bcrypt, PBKDF2): Deliberately slow and memory-hard to neutralize GPU/ASIC brute force attacks.
- Salting: Unique cryptographically random salt per user prevents rainbow table attacks.

## Do's and Don'ts

- **Do:** Use Argon2id (or bcrypt) with an appropriate work factor for all password storage.
- **Do:** Use HMAC-SHA256 for authenticating API webhooks and tamper-proofing tokens.
- **Do:** Validate file and firmware checksums against published SHA-256 digests before execution.
- **Don't:** Never use MD5 or SHA-1 for security purposes—practical collision attacks exist.
- **Don't:** Never use fast hashing algorithms (SHA-256, MD5) for password storage without slow key derivation.
- **Don't:** Never reuse salts across multiple password entries.

## Practical Implementation & Architecture

Practical implementation of these concepts involves various tools and techniques depending on specific requirements, technology stacks, and organizational constraints. Security professionals should maintain familiarity with industry-standard tools while remaining adaptable to emerging technologies and methodologies.

## Related Skills

- `security.cryptography.symmetric-vs-asymmetric-encryption`
- `security.access-control.access-control-models`
