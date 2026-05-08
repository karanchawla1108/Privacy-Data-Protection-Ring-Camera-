# Privacy Protection and Anonymization Tool

## Overview

Demonstrates privacy-preserving data processing by applying anonymization, encryption, and re-identification risk assessment to Ring camera data. Reduces re-identification risk from 100% to 0% while maintaining data utility.

## Purpose

Demonstrates all four privacy-preserving techniques for COM6020M Privacy & Data Protection:
1. Data anonymization
2. Privacy risk assessment  
3. Algorithm transparency
4. Data encryption

## What It Does

1. Takes same Ring camera data as Program 1
2. Assesses original re-identification risk: 100/100 (CRITICAL)
3. Applies anonymization techniques
4. Assesses anonymized re-identification risk: 0/100 (LOW)
5. Encrypts anonymized data
6. Exports before/after comparison (100% privacy improvement)

## Privacy Techniques Applied

### 1. Data Anonymization

**PII Removal:**
- Names, emails, exact locations: DELETED

**SHA-256 Hashing (irreversible):**
- WiFi: "HomeNetwork_2.4GHz" → "c58598cbae637f81..."
- IP: "192.168.1.100" → "2a39f1eedcd9f986..."

**Pseudonymization:**
- Device: "RING-A1B2C3D4E5" → "DEVICE-602E797C"

**Temporal Generalization:**
- "2026-04-24T08:15:23" → "2026-04-24 08:00:00" (hour-level only)

### 2. Privacy Risk Assessment

**Original Data:** 100/100 risk (name, email, location exposed)  
**Anonymized Data:** 0/100 risk (all PII removed/hashed)  
**Result:** 100% privacy improvement

### 3. Algorithm Transparency

Each step explained:
1. Delete name, email, location (prevents direct identification)
2. Hash WiFi/IP with SHA-256 (irreversible protection)
3. Pseudonymize device IDs (maintains utility without exposure)
4. Generalize timestamps (prevents exact routine tracking)

### 4. Data Encryption

XOR cipher with SHA-256 key derivation for secure storage demonstration.

## Requirements

- Python 3.6+
- No external packages (standard library only)

## Usage

```bash
python3 camera_privacy_protector.py

# Runtime: 5-10 seconds
# Output: Terminal + camera_privacy_protected_data.json
```

## Output

### JSON File Structure

**camera_privacy_protected_data.json** contains:

```json
{
  "original_data": {
    "motion_events": [
      {
        "user_name": "John Smith",
        "user_email": "john@email.com",
        "wifi_network": "HomeNetwork_2.4GHz"
      }
    ],
    "privacy_implications": "Contains PII - high re-identification risk"
  },
  
  "anonymized_data": {
    "motion_events": [
      {
        "wifi_hash": "c58598cbae637f81",
        "ip_hash": "2a39f1eedcd9f986",
        "device_pseudonym": "DEVICE-602E797C"
      }
    ],
    "techniques_applied": [
      "PII removal",
      "SHA-256 hashing",
      "Pseudonymization",
      "Temporal generalization",
      "XOR encryption"
    ],
    "privacy_implications": "PII removed - low re-identification risk"
  }
}
```

## Why Each Technique Matters

| Technique | Problem | Solution | Result |
|-----------|---------|----------|--------|
| **PII Removal** | Names/emails identify instantly | Delete all direct identifiers | Cannot identify individual |
| **Hashing** | WiFi/IP enable tracking | SHA-256 one-way hash | Cannot recover originals |
| **Pseudonymization** | Device IDs link to hardware | Replace with pseudonyms | Maintains utility without exposure |
| **Generalization** | Exact times show routine | Hour-level precision only | Prevents precise tracking |
| **Encryption** | Storage needs security | XOR cipher | Secure data at rest |

## GDPR Compliance

**Article 4(5) - Pseudonymisation**
- SHA-256 hashing (WiFi, IP)
- Device pseudonym generation

**Article 5(1)(c) - Data Minimisation**
- PII deletion (names, emails, locations)
- Only necessary fields retained

**Article 25 - Privacy by Design**
- Built-in anonymization pipeline
- Proactive privacy protection

**Article 32 - Security of Processing**
- Encryption for data at rest
- Hashing for integrity

## Example Terminal Output

```
RE-IDENTIFICATION RISK - ORIGINAL DATA
Score: 100/100 (CRITICAL)
Issues: Name, email, location, WiFi, IP all exposed

APPLYING ANONYMIZATION
Processing 17 events...
✓ PII removed
✓ Networks hashed
✓ Devices pseudonymized
✓ Timestamps generalized

RE-IDENTIFICATION RISK - ANONYMIZED DATA
Score: 0/100 (LOW)
Protection: All PII removed/hashed

PRIVACY IMPROVEMENT: 100%
```

## Applicability to Cloud Storage

**Ring's cloud storage should follow these techniques before upload to eliminate third-party access risks identified in Program 1.** If Ring anonymized data before cloud storage:
- Employee viewing would only see anonymized records
- Police requests would access de-identified data only
- Re-identification risk: 0/100 vs current 100/100
- Cloud storage penalty eliminated

## Comparison to Program 1

| Aspect | Program 1 | Program 2 |
|--------|-----------|-----------|
| **Purpose** | Identify problems | Solve problems |
| **Cloud Score** | 15/100 | N/A (applies to any storage) |
| **Re-ID Risk** | Shows 100/100 | Reduces to 0/100 |
| **Output** | 2 JSON files (cloud vs local) | 1 JSON (before/after anonymization) |
| **Focus** | Storage location matters | Anonymization protects anywhere |

**Together:** Complete privacy analysis (problem + solution)

## Key Data Transformation

**Before:**
```json
{
  "user_name": "John Smith",
  "user_email": "john.smith@email.com",
  "camera_location": "123 Main Street",
  "wifi_network": "HomeNetwork_2.4GHz",
  "ip_address": "192.168.1.100",
  "timestamp": "2026-04-24T08:30:45.123456"
}
```

**After:**
```json
{
  "wifi_hash": "c58598cbae637f81",
  "ip_hash": "2a39f1eedcd9f986",
  "device_pseudonym": "DEVICE-602E797C",
  "timestamp_hour": "2026-04-24 08:00:00",
  "anonymization_applied": true
}
```

## Limitations

- Simulated data (not real cameras)
- XOR cipher demonstration (production needs AES-256)
- Single dataset (no k-anonymity testing)
- No differential privacy (out of scope)

## Quick Start

```bash
# Run
python3 camera_privacy_protector.py

# View output
cat camera_privacy_protected_data.json
```

## GitHub Links

- **Program:** https://github.com/karanchawla1108/Privacy-Data-Protection-Ring-Camera-/blob/main/Camera%20Privacy%20Protector/camera_privacy_protector.py
- **Output JSON:** https://github.com/karanchawla1108/Privacy-Data-Protection-Ring-Camera-/blob/main/Camera%20Privacy%20Protector/camera_privacy_protected_data.json

---

**Assignment:** COM6020M Privacy & Data Protection  
**Student:** Karan Chawla  
**Institution:** St John York University
**Date:** May 2026
