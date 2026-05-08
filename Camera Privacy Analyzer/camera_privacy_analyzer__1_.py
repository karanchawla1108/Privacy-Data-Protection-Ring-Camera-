#!/usr/bin/env python3
"""
Smart Home Camera Privacy Risk Analyzer
Demonstrates privacy exposure from motion detection and continuous monitoring
For: COM6020M Privacy & Data Protection Assignment
"""

import json

from datetime import datetime, timedelta
import random
from collections import defaultdict

class SmartCameraSimulator:
    """Simulates data collection by smart home cameras like Ring, Nest, etc."""
    
    def __init__(self, camera_name="Front Door Camera", cloud_storage=True):
        self.camera_name = camera_name
        self.cloud_storage = cloud_storage
        self.motion_events = []
        self.metadata_log = []
        
    def simulate_week_activity(self):
        """Generate realistic week of motion detection events"""
        print(f"\n{'='*60}")
        print(f"SIMULATING: {self.camera_name}")
        print(f"Cloud Storage: {'ENABLED' if self.cloud_storage else 'LOCAL ONLY'}")
        print(f"{'='*60}\n")
        
        # Simulate 7 days of activity
        start_date = datetime.now() - timedelta(days=7)
        
        # Common departure/arrival times (realistic patterns)
        morning_departure = [8, 8.5, 9]  # 8am-9am
        evening_return = [17.5, 18, 18.5, 19]  # 5:30pm-7pm
        
        for day in range(7):
            current_date = start_date + timedelta(days=day)
            
            # Morning departure
            departure_hour = random.choice(morning_departure)
            self._log_motion_event(current_date, departure_hour, "person", 15)
            
            # Delivery during day (3 days/week)
            if random.random() < 0.4:
                delivery_hour = random.uniform(10, 16)
                self._log_motion_event(current_date, delivery_hour, "delivery_person", 45)
            
            # Evening return
            return_hour = random.choice(evening_return)
            self._log_motion_event(current_date, return_hour, "person", 20)
            
            # Late night activity (occasionally)
            if random.random() < 0.2:
                late_hour = random.uniform(22, 23.5)
                self._log_motion_event(current_date, late_hour, "person", 8)
                
        print(f"Total motion events logged: {len(self.motion_events)}")
        
    def _log_motion_event(self, date, hour, object_type, duration_seconds):
        """Log individual motion detection event"""
        timestamp = date.replace(hour=int(hour), minute=int((hour % 1) * 60))
        
        event = {
            "timestamp": timestamp.isoformat(),
            "camera_id": self.camera_name,
            "object_detected": object_type,
            "duration_seconds": duration_seconds,
            "snapshot_captured": True,
            "video_clip_stored": self.cloud_storage,
            "cloud_uploaded": self.cloud_storage
        }
        
        self.motion_events.append(event)
        
        # Metadata that reveals patterns
        metadata = {
            "timestamp": timestamp.isoformat(),
            "day_of_week": timestamp.strftime("%A"),
            "time_of_day": "morning" if hour < 12 else "afternoon" if hour < 18 else "evening",
            "device_online": True,
            "wifi_network": "HomeNetwork_2.4GHz",
            "ip_address": "192.168.1.100"  # Local IP
        }
        
        self.metadata_log.append(metadata)
        
    def analyze_privacy_risks(self):
        """Analyze what can be inferred from collected data"""
        print(f"\n{'='*60}")
        print("PRIVACY RISK ANALYSIS")
        print(f"{'='*60}\n")
        
        if not self.motion_events:
            print("No motion events to analyze")
            return
        
        # Pattern analysis
        patterns = self._detect_patterns()
        
        print(" CRITICAL PRIVACY EXPOSURES IDENTIFIED:\n")
        
        # 1. Daily routine patterns
        if patterns['morning_departures']:
            avg_departure = sum(patterns['morning_departures']) / len(patterns['morning_departures'])
            print(f"1. DAILY ROUTINE EXPOSED:")
            print(f"   - Typical departure time: ~{int(avg_departure):02d}:{int((avg_departure%1)*60):02d}")
            print(f"   - Regularity: {len(patterns['morning_departures'])}/7 days")
            print(f"    RISK: Burglar knows when home is empty\n")
        
        # 2. Occupancy detection
        print(f"2. HOME OCCUPANCY TRACKING:")
        print(f"   - Total motion events: {len(self.motion_events)}")
        print(f"   - Days with activity: {patterns['active_days']}/7")
        print(f"     RISK: Third parties know when you're home/away\n")
        
        # 3. Visitor frequency
        if patterns['delivery_count'] > 0:
            print(f"3. VISITOR TRACKING:")
            print(f"   - Delivery events captured: {patterns['delivery_count']}")
            print(f"     RISK: Shopping habits revealed to camera company\n")
        
        # 4. Cloud storage risks
        if self.cloud_storage:
            print(f"4. CLOUD DATA EXPOSURE:")
            print(f"   - Video clips uploaded: {len(self.motion_events)}")
            print(f"   - Stored on company servers: YES")
            print(f"   - Accessible by: Camera company, employees, contractors")
            print(f"   - Third-party access: Potentially (police, advertisers)")
            print(f"     RISK: No control over who views your footage\n")
        
        # 5. Metadata leakage
        print(f"5. METADATA PRIVACY LEAKS:")
        print(f"   - WiFi network name exposed: YES")
        print(f"   - Daily activity timestamps: {len(self.metadata_log)} records")
        print(f"   - Pattern-of-life data: COMPLETE")
        print(f"     RISK: Detailed behavioral profile created\n")
        
        # Calculate privacy score
        privacy_score = self._calculate_privacy_score(patterns)
        print(f"\n{'='*60}")
        print(f"OVERALL PRIVACY SCORE: {privacy_score}/100")
        print(f"Rating: {self._get_privacy_rating(privacy_score)}")
        print(f"{'='*60}\n")
        
    def _detect_patterns(self):
        """Detect behavioral patterns from motion events"""
        patterns = {
            'morning_departures': [],
            'evening_returns': [],
            'delivery_count': 0,
            'active_days': 0
        }
        
        days_active = set()
        
        for event in self.motion_events:
            timestamp = datetime.fromisoformat(event['timestamp'])
            hour = timestamp.hour + timestamp.minute/60
            
            # Morning departures (6am-10am)
            if 6 <= hour < 10:
                patterns['morning_departures'].append(hour)
                
            # Evening returns (5pm-8pm)
            if 17 <= hour < 20:
                patterns['evening_returns'].append(hour)
                
            # Deliveries
            if event['object_detected'] == 'delivery_person':
                patterns['delivery_count'] += 1
                
            # Track active days
            days_active.add(timestamp.date())
        
        patterns['active_days'] = len(days_active)
        return patterns
        
    def _calculate_privacy_score(self, patterns):
        """Calculate privacy score (0=worst, 100=best)"""
        score = 100
        
        # Deduct for cloud storage
        if self.cloud_storage:
            score -= 40
            
        # Deduct for pattern predictability
        if len(patterns['morning_departures']) >= 5:
            score -= 20
            
        # Deduct for metadata collection
        score -= 15
        
        # Deduct for continuous monitoring
        score -= 10
        
        return max(0, score)
        
    def _get_privacy_rating(self, score):
        """Convert score to rating"""
        if score >= 80:
            return "GOOD - Minimal privacy risk"
        elif score >= 60:
            return "MODERATE - Some privacy concerns"
        elif score >= 40:
            return "POOR - Significant privacy exposure"
        else:
            return "CRITICAL - Severe privacy violations"
            
    def generate_mitigation_report(self):
        """Suggest privacy-preserving alternatives"""
        print(f"\n{'='*60}")
        print("PRIVACY MITIGATION STRATEGIES")
        print(f"{'='*60}\n")
        
        print(" RECOMMENDED ACTIONS:\n")
        
        print("1. DISABLE CLOUD STORAGE:")
        print("   - Use local-only storage on SD card or NAS")
        print("   - Prevents third-party access to footage")
        print("   - Maintains full control over data\n")
        
        print("2. IMPLEMENT PRIVACY ZONES:")
        print("   - Mask neighbor properties from recording")
        print("   - Reduce public space capture")
        print("   - Only monitor your own property\n")
        
        print("3. MINIMIZE DATA RETENTION:")
        print("   - Delete recordings after 7-14 days")
        print("   - Reduce attack surface for breaches")
        print("   - Comply with data minimization principles\n")
        
        print("4. ENABLE ENCRYPTION:")
        print("   - Use end-to-end encryption for any cloud uploads")
        print("   - Encrypt local storage")
        print("   - Prevent unauthorized viewing\n")
        
        print("5. DISABLE UNNECESSARY FEATURES:")
        print("   - Turn off facial recognition")
        print("   - Disable audio recording if not needed")
        print("   - Limit motion detection sensitivity\n")
        
        print("6. CHOOSE PRIVACY-FIRST ALTERNATIVES:")
        print("   - Look for cameras with local-only processing")
        print("   - Avoid brands with police partnerships")
        print("   - Check company's data sharing policies\n")
        
    def export_data(self, filename="camera_data_export.json"):
        """Export collected data (demonstrates GDPR data portability)"""
        export_data = {
            "camera_name": self.camera_name,
            "export_date": datetime.now().isoformat(),
            "cloud_storage_enabled": self.cloud_storage,
            "motion_events": self.motion_events,
            "metadata_log": self.metadata_log,
            "total_events": len(self.motion_events),
            "privacy_implications": "This data reveals your daily patterns, occupancy, and habits"
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
            
        print(f"\nData exported to: {filename}")
        print(f"   This represents YOUR data under GDPR Article 15 (Right of Access)")
        print(f"   File size: {len(json.dumps(export_data))} bytes\n")

def compare_scenarios():
    """Compare privacy impact: Cloud vs Local storage"""
    print("\n" + "="*60)
    print("SCENARIO COMPARISON: CLOUD VS LOCAL STORAGE")
    print("="*60)
    
    # Scenario 1: Cloud-enabled (like Ring default)
    print("\n>>> SCENARIO 1: Cloud Storage ENABLED (Ring Default)")
    camera_cloud = SmartCameraSimulator("Ring Front Door", cloud_storage=True)
    camera_cloud.simulate_week_activity()
    camera_cloud.analyze_privacy_risks()
    
    # Scenario 2: Local-only
    print("\n\n>>> SCENARIO 2: Local Storage ONLY (Privacy-Preserving)")
    camera_local = SmartCameraSimulator("Local Camera", cloud_storage=False)
    camera_local.simulate_week_activity()
    camera_local.analyze_privacy_risks()
    
    # Mitigation strategies
    camera_cloud.generate_mitigation_report()
    
    # Export both scenarios for comparison
    camera_cloud.export_data("camera_data_export_CLOUD.json")
    camera_local.export_data("camera_data_export_LOCAL.json")

if __name__ == "__main__":
    print("""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|  SMART HOME CAMERA PRIVACY RISK ANALYZER                   |
|  COM6020M: Privacy & Data Protection                       |
|                                                            |
|  Demonstrates privacy risks from motion detection and      |
|  continuous surveillance in smart home cameras             |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
""")
    
    compare_scenarios()
    
    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}\n")
    print("Key Takeaways:")
    print("• Motion detection creates detailed behavioral profiles")
    print("• Cloud storage = loss of control over personal footage")
    print("• Metadata alone reveals daily patterns and occupancy")
    print("• Local-only storage significantly improves privacy")
    print("• Smart cameras create surveillance infrastructure\n")
