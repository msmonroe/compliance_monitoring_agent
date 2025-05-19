import smtplib
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_RECIPIENT, SMTP_SERVER, SMTP_PASSWORD

def send_email(content):
    try:
        msg = MIMEText(content)
        msg["Subject"] = "Weekly Compliance Monitoring Report"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECIPIENT

        with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
            server.login(EMAIL_SENDER, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, [EMAIL_RECIPIENT], msg.as_string())

        print("[INFO] Report email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
