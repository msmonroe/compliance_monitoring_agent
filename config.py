import os
from dotenv import load_dotenv
load_dotenv()

LOG_FILE = os.getenv("LOG_FILE", "sample_logs/server_log.csv")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
