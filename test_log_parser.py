import logging
from parsers.log_parser import load_logs
from agents.scanner_agent import filter_suspicious

logging.basicConfig(filename="audit.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TEST_LOG_PATH = "sample_logs/server_log.csv"

def test_log_parser():
    try:
        logs = load_logs(TEST_LOG_PATH)
        if logs:
            logging.info(f"[TEST PASS] Loaded {len(logs)} log entries.")
            print(f"[TEST PASS] Loaded {len(logs)} log entries.")
            print("Sample entry:", logs[0])
        else:
            logging.warning("[TEST FAIL] No log entries loaded.")
            print("[TEST FAIL] No log entries loaded.")
    except Exception as e:
        logging.exception("Error in test_log_parser.")
        print("[TEST FAIL] Exception occurred while loading logs.")

def test_filter_suspicious():
    try:
        logs = load_logs(TEST_LOG_PATH)
        suspicious = filter_suspicious(logs)
        if suspicious:
            logging.info(f"[TEST PASS] Detected {len(suspicious)} suspicious entries.")
            print(f"[TEST PASS] Detected {len(suspicious)} suspicious entries.")
            print("Sample suspicious entry:", suspicious[0])
        else:
            logging.warning("[TEST FAIL] No suspicious entries detected.")
            print("[TEST FAIL] No suspicious entries detected.")
    except Exception as e:
        logging.exception("Error in test_filter_suspicious.")
        print("[TEST FAIL] Exception occurred while filtering suspicious entries.")

if __name__ == "__main__":
    test_log_parser()
    test_filter_suspicious()
