# Privacy-Data-Protection-Ring-Camera

## Overview

Demonstrates privacy risks in Ring doorbell cameras and privacy-preserving data processing techniques through two Python programs.

**Contents:**
- Privacy risk assessment with transparent scoring
- Data anonymization and encryption implementation
- GDPR compliance demonstrations

---

## Repository Structure

```
Privacy-Data-Protection-Ring-Camera/
│
├── Camera Privacy Analyzer/
│   ├── camera_privacy_analyzer.py          # Program 1
│   ├── camera_data_export_CLOUD.json       # Cloud storage output
│   └── camera_data_export_LOCAL.json       # Local storage output
│
└── Camera Privacy Protector/
    ├── camera_privacy_protector.py         # Program 2
    └── camera_privacy_protected_data.json  # Anonymization output
```

---

## Programs

### Program 1: Privacy Risk Analyzer

**Purpose:** Quantifies Ring doorbell privacy risks

**What it does:**
- Simulates 1 week of motion detection data
- Scores privacy risks (0-100 scale)
- Compares cloud vs local storage
- Exports 2 JSON files

**Results:**
- Cloud storage: 15/100 (CRITICAL)
- Local storage: 55/100 (POOR but 267% better)
- Demonstrates GDPR Article 15 Right of Access

**Link:** [Program 1](https://github.com/karanchawla1108/Privacy-Data-Protection-Ring-Camera-/tree/main/Camera%20Privacy%20Analyzer)

---

### Program 2: Privacy Protector

**Purpose:** Demonstrates privacy-preserving techniques

**What it does:**
- Takes Program 1 data and anonymizes it
- Applies 4 techniques:
  1. PII removal (names, emails, locations)
  2. SHA-256 hashing (WiFi, IP - irreversible)
  3. Device pseudonymization
  4. Timestamp generalization + encryption

**Results:**
- Original: 100/100 re-identification risk
- Anonymized: 0/100 re-identification risk
- 100% privacy improvement

**GDPR:** Articles 4(5), 5(1)(c), 25, 32 demonstrated

**Link:** [Program 2](https://github.com/karanchawla1108/Privacy-Data-Protection-Ring-Camera-/tree/main/Camera%20Privacy%20Protector)

---

## Quick Start

```bash
# Program 1
cd "Camera Privacy Analyzer"
python3 camera_privacy_analyzer.py

# Program 2
cd "Camera Privacy Protector"
python3 camera_privacy_protector.py
```

**Requirements:** Python 3.6+, no external packages

---

## Key Findings

### Privacy Risks (Program 1)

| Factor | Impact | Score Deduction |
|--------|--------|-----------------|
| Cloud storage | Third-party access | -40 |
| Predictable patterns | Routine exposure | -20 |
| Metadata collection | Behavioral profiling | -15 |
| Continuous monitoring | Always-on surveillance | -10 |

**Cloud: 15/100 | Local: 55/100 | Improvement: 267%**

### Privacy Solutions (Program 2)

| Technique | Implementation | Result |
|-----------|---------------|--------|
| PII Removal | Delete names, emails, locations | No direct identification |
| SHA-256 Hashing | WiFi, IP addresses | Irreversible protection |
| Pseudonymization | Device IDs | Utility without exposure |
| Generalization | Hour-level timestamps | No precise tracking |

**Re-identification: 100/100 → 0/100 | Improvement: 100%**

---

## Data Transformation Example

### Before (Original):
```json
{
  "user_name": "John Smith",
  "user_email": "john@email.com",
  "camera_location": "123 Main St",
  "wifi_network": "HomeNetwork_5G",
  "timestamp": "2026-04-24T08:30:45"
}
```

### After (Anonymized):
```json
{
  "wifi_hash": "c58598cbae637f81",
  "ip_hash": "2a39f1eedcd9f986",
  "device_pseudonym": "DEVICE-602E797C",
  "timestamp_hour": "2026-04-24 08:00:00",
  "anonymization_applied": true
}
```

---

## GDPR Compliance

| Article | Requirement | Implementation |
|---------|-------------|----------------|
| 4(5) | Pseudonymisation | SHA-256 hashing |
| 5(1)(c) | Data minimisation | PII removal |
| 15 | Right of access | JSON export |
| 25 | Privacy by design | Built-in anonymization |
| 32 | Security | Encryption + hashing |

---

## Real-World Context

**Ring Employee Scandal (2019):** Unrestricted employee access to customer footage demonstrates inadequate controls

**Wyze Breach (2019):** 2.4M users' metadata exposed proves metadata alone creates privacy risks

**Ring-Police (2018+):** 2,000+ police departments partnered, enabling warrantless surveillance

**This analysis proves:** Cloud-first architecture creates inherent privacy violations; local storage + anonymization provides viable alternative

---

## Assignment Requirements Met

**Program 1:**
- ✓ Privacy risk assessment
- ✓ Algorithm transparency
- ✓ GDPR Article 15

**Program 2:**
- ✓ Data anonymization
- ✓ Privacy risk assessment
- ✓ Algorithm transparency
- ✓ Data encryption

---

## Limitations

- Simulated data (not real cameras)
- XOR cipher demonstration (production needs AES-256)
- Single-camera model (no network simulation)

---

## Author

**Karan Chawla**  
GitHub: [@karanchawla1108](https://github.com/karanchawla1108)  
Module: COM6020M Privacy & Data Protection  
St John York Universities | May 2026
