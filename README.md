# Privacy-Data-Protection-Ring-Camera

**COM6020M: Privacy & Data Protection Assignment**  
**Student:** Karan Chawla (karanchawla1108)  
**Institution:** York Business School  
**Submission Date:** May 2026

---

## Repository Overview

This repository contains coursework for COM6020M Privacy & Data Protection, demonstrating privacy risks in smart home surveillance (Ring cameras) and privacy-preserving data processing techniques.

**What's Inside:**
- Ring camera privacy risk analysis with Python implementation
- Data anonymization and encryption tools
- Privacy risk assessment methodologies
- GDPR compliance demonstrations

---

## Repository Structure

```
Privacy-Data-Protection-Ring-Camera/
│
├── README.md                                    # This file
│
├── Camera Privacy Analyzer/
│   ├── README.md                                # Program 1 documentation
│   ├── camera_privacy_analyzer__1_.py           # Privacy risk assessment tool
│   └── camera_data_export.json                  # Example output (privacy violations)
│
└── Camera Privacy Protector/
    ├── README.md                                # Program 2 documentation
    ├── camera_privacy_protector.py              # Anonymization & encryption tool
    └── camera_privacy_protected_data.json       # Example output (before/after)
```

---

## Programs Overview

### Program 1: Camera Privacy Analyzer

**File:** `camera_privacy_analyzer__1_.py`

**Purpose:** Quantify privacy risks in Ring doorbell cameras

**What it does:**
- Simulates 1 week of Ring camera motion detection data
- Implements transparent privacy scoring algorithm (0-100 scale)
- Compares cloud storage vs local-only configurations
- Exports data demonstrating GDPR Article 15 Right of Access

**Key Results:**
- **Cloud storage (Ring default):** 15/100 privacy score (CRITICAL)
- **Local storage only:** 55/100 privacy score (POOR but 267% better)
- **Findings:** Motion timestamps alone expose daily routines, shopping habits, behavioral profiles

**Technologies:** Python 3.6+, no external dependencies

---

### Program 2: Camera Privacy Protector

**File:** `camera_privacy_protector.py`

**Purpose:** Demonstrate privacy-preserving data processing

**What it does:**
- Takes same camera data as Program 1
- Applies 4 privacy techniques:
  1. **Data anonymization** - Removes PII (names, emails, locations)
  2. **Privacy risk assessment** - Measures re-identification risk
  3. **Algorithm transparency** - Explains each anonymization step
  4. **Data encryption** - XOR cipher with SHA-256 key derivation

**Key Results:**
- **Original data:** 100/100 re-identification risk (CRITICAL)
- **Anonymized data:** 0/100 re-identification risk (LOW)
- **Privacy improvement:** 100% re-identification prevention

**GDPR Compliance:**
- Article 4(5): Pseudonymisation (SHA-256 hashing)
- Article 5(1)(c): Data minimisation (PII removal)
- Article 25: Privacy by design (built-in anonymization)
- Article 32: Security of processing (encryption)

**Technologies:** Python 3.6+, no external dependencies

---

## How to Run

### Prerequisites
```bash
# Python 3.6 or higher required
python3 --version
```

### Program 1 - Privacy Risk Analyzer
```bash
cd "Camera Privacy Analyzer"
python3 camera_privacy_analyzer__1_.py

# Output:
# - Terminal: Privacy risk analysis
# - Output File: camera_data_export.json
```

### Program 2 - Privacy Protector
```bash
cd "Camera Privacy Protector"
python3 camera_privacy_protector.py

# Output:
# - Terminal: Before/after anonymization comparison
# - Output File: camera_privacy_protected_data.json
```

**Runtime:** 5-10 seconds each

---

## Key Findings Summary

### Privacy Risks Identified (Program 1)

| Risk Factor | Impact | Points Deducted |
|-------------|--------|-----------------|
| Cloud storage enabled | Third-party data access | -40 |
| Predictable daily patterns | Routine exposure for burglars | -20 |
| Metadata collection | Behavioral profiling | -15 |
| Continuous monitoring | Always-on surveillance | -10 |

**Total Privacy Score:**
- Cloud: 15/100 (CRITICAL VIOLATIONS)
- Local: 55/100 (POOR but acceptable)

### Privacy Solutions Demonstrated (Program 2)

| Technique | Method | Result |
|-----------|--------|--------|
| PII Removal | Delete names, emails, locations | Direct identification prevented |
| Hashing | SHA-256 (WiFi, IP addresses) | Irreversible protection |
| Pseudonymization | Hash-based device IDs | Maintains utility without exposure |
| Generalization | Hour-level timestamps | Prevents precise routine tracking |
| Encryption | XOR cipher + SHA-256 key | Secure data storage |

**Re-identification Risk Reduction:** 100/100 → 0/100 (100% improvement)

---

## Technical Details

### Data Structures

**Motion Event (Original):**
```json
{
  "timestamp": "2026-04-24T08:30:00",
  "user_name": "John Smith",
  "user_email": "john@email.com",
  "camera_location": "Front Door, 123 Main St",
  "wifi_network": "HomeNetwork_5G",
  "ip_address": "192.168.1.100",
  "object_detected": "person"
}
```

**Motion Event (Anonymized):**
```json
{
  "timestamp_hour": "2026-04-24 08:00:00",
  "wifi_hash": "c58598cbae637f81...",
  "ip_hash": "2a39f1eedcd9f986...",
  "device_pseudonym": "DEVICE-602E797C",
  "object_detected": "person",
  "anonymization_applied": true
}
```

### Privacy Scoring Algorithm

**Transparent calculation:**
```
Initial Score: 100 (perfect privacy)

IF cloud_storage_enabled:
    score -= 40  (loss of data control)

IF predictable_patterns (5+ identical daily events):
    score -= 20  (routine exposure)

IF metadata_collected (WiFi, IP, device info):
    score -= 15  (behavioral profiling)

IF continuous_monitoring:
    score -= 10  (always-on surveillance)

Final Score: 0-100
```

**Rating Scale:**
- 80-100: GOOD - Minimal privacy risk
- 60-79: MODERATE - Some concerns
- 40-59: POOR - Significant exposure
- 20-39: CRITICAL - Severe violations
- 0-19: SEVERE - Extreme risk

---

## Academic Context

### Assignment Requirements Met

**Program 1 demonstrates:**
- Privacy risk assessment methodology
- Transparent algorithm design
- GDPR Article 15 (Right of Access)

**Program 2 demonstrates:**
1. Data anonymization (PII removal, hashing, pseudonymization)
2. Privacy risk assessment (re-identification analysis)
3. Algorithm transparency (explainable processing)
4. Data encryption (secure storage methods)

### GDPR Compliance

| Article | Requirement | Implementation |
|---------|-------------|----------------|
| 4(5) | Pseudonymisation | SHA-256 hashing, pseudonym generation |
| 5(1)(c) | Data minimisation | PII removal, essential fields only |
| 15 | Right of access | JSON export functionality |
| 25 | Privacy by design | Built-in anonymization pipeline |
| 32 | Security of processing | Encryption, hashing, access controls |

---

## Real-World Impact

### Case Studies Referenced

**Ring Employee Access Scandal (2019)**
- Employees had unrestricted access to customer video feeds
- Demonstrates inadequate access controls
- Encryption added only after scandal (reactive, not proactive)

**Wyze Data Breach (2019)**
- 2.4 million users' metadata exposed
- WiFi names, IP addresses, camera locations leaked
- Proves metadata alone creates significant privacy exposure

**Ring-Police Partnerships (2018-Present)**
- 2,000+ US police departments partnered with Ring
- Warrantless footage requests enabled
- Creates privatized surveillance infrastructure

**Findings from this analysis:**
- Metadata privacy violations occur even without video access
- Cloud-first architecture creates inherent privacy risks
- Local storage provides 267% privacy improvement

---

## Use Cases

### For Students
- Privacy risk quantification methodology
- GDPR compliance implementation examples
- Data anonymization techniques

### For Researchers
- Baseline privacy scoring framework
- Surveillance system comparison methodology
- Privacy-enhancing technology demonstrations

### For Privacy Advocates
- Evidence of Ring doorbell privacy violations
- Technical solutions for privacy protection
- Policy recommendation support materials

---

## Limitations

- **Simulated data:** Not connected to real Ring cameras
- **Simplified scoring:** Real-world may have additional risk factors
- **XOR cipher:** Demonstration only (production should use AES-256)
- **Single-camera:** Does not model interconnected camera networks

---



## Author

**Karan Chawla**  
GitHub: [@karanchawla1108](https://github.com/karanchawla1108)  
Module: COM6020M Privacy & Data Protection  
Institution: York Business School  
Date: May 2026



