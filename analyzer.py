import re
from collections import Counter

def read_logs(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def parse_logs(logs):
    log_data = []

    for line in logs:
        match = re.match(r"(.+?)\s+(INFO|ERROR|WARNING)\s+(.*)", line)
        if match:
            timestamp, level, message = match.groups()
            log_data.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    return log_data

def count_log_levels(log_data):
    levels = [log["level"] for log in log_data]
    return Counter(levels)

def detect_anomalies(log_data, threshold=3):
    error_messages = [log["message"] for log in log_data if log["level"] == "ERROR"]
    error_count = Counter(error_messages)

    anomalies = {msg: count for msg, count in error_count.items() if count >= threshold}

    return anomalies

def generate_report(log_data):
    counts = count_log_levels(log_data)
    anomalies = detect_anomalies(log_data)

    print("\n📊 LOG SUMMARY")
    print("-------------------")
    print(f"INFO: {counts.get('INFO', 0)}")
    print(f"WARNING: {counts.get('WARNING', 0)}")
    print(f"ERROR: {counts.get('ERROR', 0)}")

    print("\n🚨 ANOMALY DETECTION")
    print("-------------------")

    if anomalies:
        for msg, count in anomalies.items():
            print(f"High occurrence of '{msg}' → {count} times")
    else:
        print("No anomalies detected")