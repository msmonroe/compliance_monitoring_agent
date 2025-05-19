from collections import defaultdict

def filter_suspicious(logs):
    suspicious = []
    failed_attempts = defaultdict(int)

    for entry in logs:
        ip = entry.get("ip")
        status = entry.get("status", "").upper()
        username = entry.get("username", "")

        if status == "FAILED":
            failed_attempts[ip] += 1

        # Rule 1: 3 or more failed logins from same IP
        if failed_attempts[ip] >= 3:
            suspicious.append(entry)

        # Rule 2: Access to sensitive accounts
        if username.lower() in ["admin", "root"] and status == "FAILED":
            suspicious.append(entry)

    # Deduplicate entries
    seen = set()
    result = []
    for entry in suspicious:
        key = (entry['timestamp'], entry['username'], entry['ip'], entry['action'])
        if key not in seen:
            seen.add(key)
            result.append(entry)

    return result
