# Privacy Protection and Anonymization Tool

## Overview

This program demonstrates privacy-preserving data processing by applying anonymization, encryption, and re-identification risk assessment to smart camera surveillance data. It shows how privacy protections can reduce re-identification risk from 100% to 0% while maintaining data utility.

## Purpose

Assignment requirement: Demonstrate all four privacy-preserving techniques for COM6020M Privacy & Data Protection coursework:
1. Data anonymization
2. Privacy risk assessment  
3. Algorithm transparency
4. Data encryption

## What It Does

1. Simulates Ring camera data collection (same as Program 1)
2. Assesses re-identification risk in original data (100/100)
3. Applies privacy-preserving anonymization techniques
4. Assesses re-identification risk in anonymized data (0/100)
5. Encrypts anonymized data for secure storage
6. Exports before/after comparison demonstrating 100% privacy improvement

## Key Features

### 1. Data Anonymization

**Techniques Applied:**

**PII Removal**
- User names: DELETED
- Email addresses: DELETED  
- Exact camera locations: DELETED
- Prevents direct identification

**SHA-256 Hashing** (irreversible)
- WiFi network names: "HomeNetwork_5G" → "c58598cbae637f81..."
- IP addresses: "192.168.1.100" → "2a39f1eedcd9f986..."
- Cannot recover original values

**Pseudonymization**
- Device serials: "RING-A1B2C3D4E5" → "DEVICE-602E797C"
- Hash-based pseudonym generation
- Maintains analytical utility

**Temporal Generalization**
- Exact timestamps: "2026-04-24T08:15:23" → "2026-04-24 08:00:00"
- Hour-level precision only
- Prevents precise routine tracking

### 2. Privacy Risk Assessment

**Re-identification Risk Scoring:**

**Original Data:**
- Direct identifiers present (name, email, location)
- Network identifiers in plaintext (WiFi, IP)
- Exact timestamps reveal routines
- **Risk Score: 100/100 (CRITICAL)**

**Anonymized Data:**
- All PII removed
- Network data hashed (irreversible)
- Timestamps generalized
- **Risk Score: 0/100 (LOW)**

**Privacy Improvement: 100% re-identification prevention**

### 3. Algorithm Transparency

Every anonymization step is explained:

**Step 1: PII Removal**
```
Original: name="John Smith", email="john@email.com"
Result: Fields deleted
Explanation: Direct identifiers enable instant identification
```

**Step 2: Network Hashing**
```
Original: wifi="HomeNetwork_5G"
Result: wifi_hash="c58598cbae637f81..."
Algorithm: SHA-256 one-way hash
Explanation: Cannot reverse to get original network name
```

**Step 3: Pseudonymization**
```
Original: device="RING-12345"
Result: device="DEVICE-602E797C"
Algorithm: Hash first 8 chars of SHA-256
Explanation: Maintains uniqueness without revealing original
```

**Step 4: Generalization**
```
Original: "2026-04-24T08:15:23"
Result: "2026-04-24 08:00:00"
Method: Truncate to hour-level
Explanation: Prevents exact routine tracking
```

### 4. Data Encryption

**XOR Cipher with SHA-256 Key Derivation**

```
Password: "privacy_protection_key_2026"
Key Generation: SHA-256(password) → 256-bit key
Encryption: XOR cipher
Result: Encrypted hex string
```

Demonstrates encryption/decryption capabilities for secure data storage.

## Requirements

- Python 3.6 or higher
- No external packages required (uses standard library only)

## Installation

```bash
# No installation needed
# Uses Python standard library only
```

## Usage

```bash
# Run the privacy protector
python3 camera_privacy_protector.py

# Expected runtime: 5-10 seconds
# Output: Terminal analysis + camera_privacy_protected_data.json
```

## Output

### Terminal Output

Displays complete before/after analysis:
1. Simulation of camera data collection
2. Re-identification risk assessment (original data)
3. Anonymization process with step-by-step explanations
4. Re-identification risk assessment (anonymized data)
5. Encryption demonstration
6. Privacy improvement summary

### JSON Export

File: `camera_privacy_protected_data.json`

Contains two sections:

**Original Data Section:**
```json
{
  "original_data": {
    "motion_events": [...],  // Contains PII
    "privacy_implications": "High re-identification risk"
  }
}
```

**Anonymized Data Section:**
```json
{
  "anonymized_data": {
    "motion_events": [...],  // PII removed/hashed
    "techniques_applied": [...],
    "privacy_implications": "Low re-identification risk"
  }
}
```

Enables direct before/after comparison.

## Privacy Techniques Explained

### Why Each Technique Matters

**1. PII Removal**
- **Problem:** Names and emails enable instant identification
- **Solution:** Complete deletion of direct identifiers
- **Result:** Cannot identify individual from remaining data

**2. Hashing**
- **Problem:** WiFi names and IPs enable device tracking
- **Solution:** SHA-256 one-way hash (irreversible)
- **Result:** Original values cannot be recovered

**3. Pseudonymization**  
- **Problem:** Device serials link events to specific hardware
- **Solution:** Replace with consistent pseudonyms
- **Result:** Maintains analytical utility without revealing device

**4. Generalization**
- **Problem:** Exact timestamps expose precise daily routines
- **Solution:** Reduce precision to hour-level
- **Result:** Prevents tracking exact arrival/departure times

**5. Encryption**
- **Problem:** Anonymized data still needs secure storage
- **Solution:** XOR encryption with key derivation
- **Result:** Additional security layer for data at rest

## GDPR Compliance

### Articles Demonstrated

**Article 4(5) - Pseudonymisation**
```
Definition: Processing personal data such that it can no longer 
be attributed to a specific data subject without additional 
information.

Implementation:
- SHA-256 hashing of network identifiers
- Hash-based pseudonym generation for devices
- Separation of identifiers from analytical data
```

**Article 5(1)(c) - Data Minimisation**
```
Principle: Personal data shall be adequate, relevant and limited 
to what is necessary.

Implementation:
- Deletion of names, emails, exact locations
- Removal of unnecessary identifying fields
- Retention only of data needed for analysis
```

**Article 25 - Data Protection by Design**
```
Requirement: Implement appropriate technical measures to ensure 
data protection principles.

Implementation:
- Built-in anonymization pipeline
- Default privacy-protective settings
- Proactive rather than reactive privacy
```

**Article 32 - Security of Processing**
```
Requirement: Implement appropriate technical measures to ensure 
security of processing.

Implementation:
- Encryption of data at rest
- Hashing for data integrity
- Access control through key management
```

## Example Output

```
============================================================
RE-IDENTIFICATION RISK ASSESSMENT - ORIGINAL DATA
============================================================

CRITICAL PII EXPOSURES IDENTIFIED:

1. DIRECT IDENTIFIERS:
   - User name: John Smith
   - User email: john.smith@email.com
   - RISK: Instant identification possible

2. NETWORK IDENTIFIERS:
   - WiFi network: HomeNetwork_2.4GHz
   - IP address: 192.168.1.100
   - RISK: Device fingerprinting enables tracking

============================================================
RE-IDENTIFICATION RISK SCORE: 100/100
RISK LEVEL: CRITICAL - Individual easily identifiable
============================================================


============================================================
APPLYING DATA ANONYMIZATION TECHNIQUES
============================================================

ALGORITHM TRANSPARENCY - Anonymization Steps:
1. PII Removal: Delete name, email, exact location
2. Hashing: SHA-256 one-way hash for WiFi, IP
3. Pseudonymization: Replace device ID with pseudonym
4. Generalization: Reduce timestamp to hour-level
5. Data Minimization: Keep only necessary fields

Processing 17 events...
  ✓ Processed 5/17 events
  ✓ Processed 10/17 events
  ✓ Processed 15/17 events
  ✓ Processed 17/17 events

============================================================
ANONYMIZATION COMPLETE: 17 records processed
============================================================


============================================================
RE-IDENTIFICATION RISK ASSESSMENT - ANONYMIZED DATA
============================================================

PRIVACY PROTECTIONS IN ANONYMIZED DATA:

1. DIRECT IDENTIFIERS:
   - User name: REMOVED ✓
   - User email: REMOVED ✓
   - Direct identification prevented (-80 risk)

2. NETWORK IDENTIFIERS:
   - WiFi: c58598cbae637f81... (HASHED) ✓
   - IP: 2a39f1eedcd9f986... (HASHED) ✓
   - Irreversible protection applied (-15 risk)

============================================================
RE-IDENTIFICATION RISK SCORE: 0/100
RISK LEVEL: LOW - Individual cannot be identified
============================================================


============================================================
PRIVACY IMPROVEMENT SUMMARY
============================================================
Original re-identification risk:    100/100
Anonymized re-identification risk:  0/100
Risk reduction:                     100 points
Privacy improvement:                100.0%
============================================================
```

## Use Cases

### For Students
- Demonstrates all 4 required privacy techniques
- Shows GDPR compliance implementation
- Provides evidence for coursework reports
- Illustrates privacy-preserving data processing

### For Developers
- Reference implementation for anonymization pipeline
- GDPR Article 4(5) pseudonymization example
- Practical encryption demonstration
- Before/after risk assessment methodology

### For Privacy Officers
- Template for privacy impact assessments
- Data minimization implementation guide
- Re-identification risk quantification
- GDPR compliance documentation

## Technical Implementation


### Key Functions

```python
apply_anonymization()
- Removes PII fields
- Applies hashing to network identifiers
- Generates pseudonyms for devices
- Generalizes temporal data

assess_re_identification_risk()
- Quantifies privacy exposure
- Compares before/after states
- Provides risk scoring

apply_encryption()
- Generates encryption key
- Encrypts anonymized data
- Demonstrates secure storage
```

## Limitations

- Simulated data (not connected to real cameras)
- XOR cipher is demonstration only (production should use AES-256)
- Single-user dataset (does not test k-anonymity across users)
- Does not implement differential privacy (out of scope)

## Future Enhancements

Potential improvements:
- AES-256 encryption instead of XOR
- K-anonymity implementation (k=5)
- L-diversity for sensitive attributes
- Differential privacy for aggregate statistics
- Federated learning integration

## Comparison to Program 1

**Program 1 (Risk Analyzer):**
- Identifies privacy problems
- Quantifies risks (15/100 for cloud)
- Demonstrates violations

**Program 2 (Privacy Protector):**
- Solves privacy problems
- Applies protections (0/100 risk achieved)
- Demonstrates solutions

**Together:** Problem identification + Solution implementation = Complete privacy analysis

## References

**Privacy-Enhancing Technologies:**
- SHA-256 Hashing (NIST FIPS 180-4)
- Pseudonymization (GDPR Article 4(5))
- K-anonymity (Sweeney, 2002)
- Differential Privacy (Dwork, 2006)

**Regulatory Frameworks:**
- GDPR Regulation (EU) 2016/679
- ISO/IEC 27701:2019 Privacy Information Management
- NIST Privacy Framework v1.0



