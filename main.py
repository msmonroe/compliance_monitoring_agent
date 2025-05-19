import logging
from config import LOG_FILE
from parsers.log_parser import load_logs
from agents.scanner_agent import filter_suspicious
from agents.analysis_agent import analyze_with_llm
from agents.report_agent import generate_report
from dispatcher.emailer import send_email

logging.basicConfig(filename="audit.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def run_compliance_check():
    try:
        logging.info("Starting compliance check process.")

        logging.info("Loading logs...")
        log_entries = load_logs(LOG_FILE)
        if not log_entries:
            logging.warning("No logs found or failed to load logs.")
            return

        logging.info("Filtering suspicious entries...")
        suspicious = filter_suspicious(log_entries)
        if not suspicious:
            logging.info("No suspicious activity detected.")
            return

        logging.info("Analyzing suspicious entries with LLM...")
        summary = analyze_with_llm(suspicious)

        logging.info("Generating compliance report...")
        report = generate_report(suspicious, summary)

        logging.info("Dispatching report via email...")
        send_email(report)

        logging.info("Compliance check completed successfully.")

    except Exception as e:
        logging.exception("Compliance check failed.")


if __name__ == "__main__":
    run_compliance_check()
