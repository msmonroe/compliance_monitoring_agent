def generate_report(entries, summary):
    report_lines = ["Compliance Monitoring Report", "=" * 30, ""]
    report_lines.append("Suspicious Log Entries:")
    for entry in entries:
        line = f"{entry['timestamp']} | {entry['username']} | {entry['action']} | {entry['ip']} | {entry['status']} | {entry['message']}"
        report_lines.append(line)

    report_lines.append("\nSummary:")
    report_lines.append(summary)

    return "\n".join(report_lines)
