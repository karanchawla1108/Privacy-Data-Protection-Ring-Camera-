# Privacy Risk Assessment Tool

## Overview

This program simulates smart home camera data collection (like Ring doorbells) and quantifies privacy risks through transparent scoring algorithms. It demonstrates how cloud-based surveillance creates measurable privacy violations compared to local-only storage alternatives.

## Purpose

Assignment requirement: Demonstrate privacy risk assessment and algorithm transparency for COM6020M Privacy & Data Protection coursework.

## What It Does

1. Simulates one week of Ring doorbell motion detection events
2. Generates realistic behavioral patterns (morning departures, evening returns, deliveries)
3. Calculates privacy scores based on identified risks
4. Compares cloud storage vs local-only storage configurations
5. Exports data demonstrating GDPR Article 15 Right of Access

## Key Features

### Data Simulation
- 7 days of realistic motion detection events
- Morning departure patterns (8-9am)
- Evening return patterns (5:30-7pm)
- Delivery events (3-4 per week)
- Occasional late-night activity

### Privacy Risk Scoring

**Transparent Algorithm:**
- Starts at 100 (perfect privacy)
- Deducts points for each identified risk:
  - Cloud storage enabled: -40 points
  - Predictable daily patterns: -20 points
  - Metadata collection: -15 points
  - Continuous monitoring: -10 points

**Risk Categories:**
- 80-100: GOOD - Minimal privacy risk
- 60-79: MODERATE - Some privacy concerns
- 40-59: POOR - Significant privacy exposure
- 20-39: CRITICAL - Severe privacy violations
- 0-19: SEVERE - Extreme privacy risk

### Scenario Comparison

**Scenario 1: Cloud Storage (Ring Default)**
- Privacy Score: 15/100
- Rating: SEVERE
- Issues: Third-party data access, employee viewing, police partnerships

**Scenario 2: Local Storage Only**
- Privacy Score: 55/100
- Rating: POOR (but 267% better than cloud)
- Improvement: Eliminates third-party access risk

## Requirements

- Python 3.6 or higher
- No external packages required (uses standard library only)

## Installation

```bash
# No installation needed - uses Python standard library
# Just download the script
```

## Usage

```bash
# Run the analyzer
python3 camera_privacy_analyzer.py

# Expected runtime: 5-10 seconds
# Output: Terminal analysis + camera_data_export.json
```

## Output

### Terminal Output

Displays:
- Simulation progress
- Privacy risk analysis with detailed breakdown
- Cloud vs Local comparison
- Mitigation recommendations
- GDPR compliance notes

### JSON Export

File: `camera_data_export.json`

Contains:
- All simulated motion events with timestamps
- Metadata log (WiFi, IP, device info)
- Total event count
- Privacy implications summary

Demonstrates GDPR Article 15 (Right of Access) - shows what data cameras actually collect.

## Privacy Risks Identified

### 1. Daily Routine Exposure
**Finding:** Morning departures detected 7/7 days at consistent times
**Risk:** Burglars can predict when home is empty
**Impact:** -20 points

### 2. Cloud Data Exposure  
**Finding:** All video clips uploaded to manufacturer servers
**Risk:** Amazon employees, contractors, police can access footage
**Impact:** -40 points

### 3. Metadata Privacy Leaks
**Finding:** WiFi network names, IP addresses, device serials logged
**Risk:** Device fingerprinting enables tracking across networks
**Impact:** -15 points

### 4. Occupancy Tracking
**Finding:** Motion events create complete presence/absence profile
**Risk:** Third parties know when you're home or away
**Impact:** -10 points

### 5. Behavioral Profiling
**Finding:** Delivery patterns reveal shopping habits
**Risk:** Commercial exploitation of behavioral data
**Impact:** Included in metadata risk

## GDPR Compliance

### Articles Addressed

**Article 5(1)(c) - Data Minimization**
- Demonstrates excessive data collection by default cameras
- Shows metadata alone creates privacy violations

**Article 15 - Right of Access**
- JSON export provides complete data access
- Demonstrates what users can request from manufacturers

**Article 32 - Security of Processing**
- Identifies inadequate access controls (cloud storage)
- Shows local storage reduces security risks

## Technical Implementation Details

### Data Structures

**Motion Event:**
```python
{
  "timestamp": "2026-04-24T08:30:00",
  "camera_id": "Ring Front Door",
  "object_detected": "person",
  "duration_seconds": 15,
  "cloud_uploaded": true
}
```

**Metadata:**
```python
{
  "timestamp": "2026-04-24T08:30:00",
  "day_of_week": "Friday",
  "wifi_network": "HomeNetwork_2.4GHz",
  "ip_address": "192.168.1.100"
}
```

### Algorithm Transparency

The scoring algorithm is fully explainable:

1. Initialize score at 100 (perfect privacy)
2. For each privacy risk detected, subtract defined points
3. Apply maximum floor of 0 (cannot go negative)
4. Map final score to privacy rating category

All deductions are logged and explained in output.

## Example Output

```
============================================================
PRIVACY RISK ASSESSMENT
============================================================

1. DAILY ROUTINE EXPOSED:
   - Typical departure time: ~08:34
   - Regularity: 7/7 days
   - Risk: Burglar knows when home is empty

2. CLOUD DATA EXPOSURE:
   - Video clips uploaded: 18
   - Accessible by: Camera company, employees, contractors
   - Risk: No control over who views your footage

3. METADATA PRIVACY LEAKS:
   - WiFi network name exposed: YES
   - Daily activity timestamps: 18 records
   - Risk: Detailed behavioral profile created

============================================================
OVERALL PRIVACY SCORE: 15/100
Rating: CRITICAL - Severe privacy violations
============================================================
```

## Use Cases

### For Students
- Demonstrates privacy risk quantification
- Shows algorithm transparency principles
- Provides evidence for privacy analysis reports
- Illustrates GDPR compliance mechanisms

### For Researchers
- Baseline privacy scoring methodology
- Comparison framework for surveillance systems
- Data minimization principles demonstration

### For Privacy Advocates
- Quantifies Ring doorbell privacy violations
- Provides evidence for policy recommendations
- Demonstrates technical privacy solutions

## Limitations

- Simulated data (not connected to real cameras)
- Simplified scoring model (real-world may have more factors)
- Does not analyze actual video content (focuses on metadata)
- Single-camera simulation (does not model camera networks)

## Future Enhancements

Potential improvements:
- Multi-camera network simulation
- Integration with actual camera APIs
- Machine learning pattern detection
- Extended GDPR compliance reporting
- Privacy nutrition label generation

## References

**Privacy Frameworks:**
- GDPR Regulation (EU) 2016/679
- ICO Domestic CCTV Guidance
- NIST Privacy Framework

**Case Studies:**
- Ring employee access scandal (2019)
- Ring-police partnerships (2018-present)
- Wyze data breach (2019)

## License

Academic coursework - All rights reserved.
Not for commercial use without permission.

## Author

Student submission for COM6020M Privacy & Data Protection
York Business School
May 2026
