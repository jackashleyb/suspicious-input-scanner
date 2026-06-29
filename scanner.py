from datetime import datetime

user_input = input("Enter text to scan: ")

patterns = {
    "SQL Injection": {
        "indicators": ["OR 1=1", "DROP TABLE", "SELECT * FROM"],
        "score": 50
    },

    "XSS Attack": {
        "indicators": ["<script>", "javascript:"],
        "score": 40
    },

    "Command Injection": {
        "indicators": ["; rm", "&&"],
        "score": 60
    }
}

risk_score = 0
detections = []

for attack_type, data in patterns.items():
    for indicator in data["indicators"]:
        if indicator.lower() in user_input.lower():
            risk_score += data["score"]
            detections.append(attack_type)


if risk_score >= 70:
    severity = "HIGH"
elif risk_score >= 40:
    severity = "MEDIUM"
elif risk_score > 0:
    severity = "LOW"
else:
    severity = "NONE"

print("\n=== SECURITY SCAN REPORT ===")
print("Input:", user_input)
print("Risk Score:", risk_score)
print("Severity:", severity)

if detections:
    print("\nThreats Detected:")
    for d in set(detections):
        print("-", d)
else:
    print("\nNo threats detected.")
    
    
    log_entry = f"""
Time: {datetime.now()}
Input: {user_input}
Risk Score: {risk_score}
Severity: {severity}
Threats: {', '.join(set(detections)) if detections else 'None'}
--------------------------
"""

with open("scan_log.txt", "a") as file:
    file.write(log_entry)