# Privacy Risk Assessment Tool

## Overview

Simulates Ring doorbell data collection and quantifies privacy risks through transparent scoring. Compares cloud storage (Ring default) vs local-only storage to demonstrate measurable privacy violations.

## Purpose

Demonstrates privacy risk assessment and algorithm transparency for COM6020M Privacy & Data Protection coursework.

## What It Does

1. Simulates one week of Ring motion detection (morning departures, evening returns, deliveries)
2. Calculates privacy scores using transparent algorithm
3. Compares cloud vs local storage configurations
4. Exports TWO JSON files for comparison

## Privacy Scoring Algorithm

**Starts at 100 (perfect privacy), deducts points for risks:**
- Cloud storage enabled: -40 points
- Predictable daily patterns: -20 points
- Metadata collection: -15 points
- Continuous monitoring: -10 points

**Rating Scale:**
- 80-100: GOOD
- 60-79: MODERATE
- 40-59: POOR
- 20-39: CRITICAL
- 0-19: SEVERE

## Requirements

- Python 3.6+
- No external packages (standard library only)

## Usage

```bash
python3 camera_privacy_analyzer.py

# Runtime: 5-10 seconds
# Creates 2 JSON files + terminal output
```

## Output Files

### File 1: camera_data_export_CLOUD.json

**Scenario:** Ring default (cloud storage ENABLED)

```json
{
  "cloud_storage_enabled": true,
  "motion_events": [
    {
      "cloud_uploaded": true,
      "video_clip_stored": true
    }
  ]
}
```

**Privacy Score:** 15/100 (SEVERE)

**Issues:** All data uploaded to Amazon servers, accessible by Ring employees/contractors/police, WiFi/IP exposed, exact timestamps reveal routine.

**File size:** 7.4 KB

---

### File 2: camera_data_export_LOCAL.json

**Scenario:** Local storage ONLY (cloud disabled)

```json
{
  "cloud_storage_enabled": false,
  "motion_events": [
    {
      "cloud_uploaded": false,
      "video_clip_stored": false
    }
  ]
}
```

**Privacy Score:** 55/100 (POOR but improved)

**Improvements:** No cloud uploads, no third-party access, Ring employees cannot view, police cannot request.

**Remaining risks:** Metadata still collected locally, routine patterns visible if device compromised.

**File size:** 6.6 KB

---

## Comparison

| Feature | Cloud JSON | Local JSON |
|---------|-----------|------------|
| **cloud_uploaded** | true | false |
| **Privacy Score** | 15/100 | 55/100 |
| **Third-party Access** | Yes | No |
| **Employee Viewing** | Possible | Not possible |
| **Privacy Improvement** | Baseline | +267% |

**267% calculation:** (55-15)/15 × 100% = 267%

## Privacy Risks Identified

**1. Cloud Data Exposure** (-40 points)
- Present in: Cloud JSON only
- Risk: Third-party access to all footage

**2. Daily Routine Exposure** (-20 points)
- Present in: Both files
- Risk: Predictable patterns (7/7 days identical)

**3. Metadata Leaks** (-15 points)
- Present in: Both files
- Risk: WiFi/IP enable device tracking

**4. Continuous Monitoring** (-10 points)
- Present in: Both files
- Risk: Always-on surveillance

## GDPR Compliance

**Article 5(1)(c) - Data Minimization**
- Cloud JSON shows excessive collection
- Local JSON shows improved minimization

**Article 15 - Right of Access**
- Both files demonstrate data export
- Shows 7KB+ weekly accumulation

**Article 32 - Security**
- Cloud JSON shows inadequate controls
- Local JSON improves security through isolation

## What the Files Prove

**Cloud JSON proves:**
- Ring uploads all motion events by default
- Third-party access enabled
- Privacy score: 15/100

**Local JSON proves:**
- Same functionality without cloud uploads
- Privacy improves to 55/100 (267% better)
- Alternative exists

**Together:**
- Ring's default maximizes data collection
- Single architectural change significantly improves privacy
- GDPR data minimization principles violated by default

## Example Terminal Output

```
>>> SCENARIO 1: Cloud Storage ENABLED (Ring Default)
Cloud Storage: ENABLED
Total events: 16

OVERALL PRIVACY SCORE: 15/100
Rating: SEVERE

>>> SCENARIO 2: Local Storage ONLY
Cloud Storage: LOCAL ONLY
Total events: 16

OVERALL PRIVACY SCORE: 55/100
Rating: POOR (267% improvement)

Data exported to: camera_data_export_CLOUD.json
Data exported to: camera_data_export_LOCAL.json
```

## Key Data Structures

**Cloud Event:**
```python
{
  "timestamp": "2026-04-24T08:30:00",
  "cloud_uploaded": true,
  "wifi_network": "HomeNetwork_2.4GHz",
  "ip_address": "192.168.1.100"
}
```

**Local Event:**
```python
{
  "timestamp": "2026-04-24T08:30:00",
  "cloud_uploaded": false,
  "wifi_network": "HomeNetwork_2.4GHz",
  "ip_address": "192.168.1.100"
}
```

## Limitations

- Simulated data (not real cameras)
- Simplified scoring (real-world has more factors)
- Metadata collected in both scenarios (only upload differs)
- Single camera (not network simulation)

## Quick Start

```bash
# Run
python3 camera_privacy_analyzer.py

# View outputs
cat camera_data_export_CLOUD.json
cat camera_data_export_LOCAL.json
```

kranchawla1108/Privacy-Data-Protection-Ring-Camera-/blob/main/Camera%20Privacy%20Analyzer/camera_data_export_LOCAL.json

---

**Assignment:** COM6020M Privacy & Data Protection  
**Student:** Karan Chawla  
**Institution:** St John York University
**Date:** May 2026
