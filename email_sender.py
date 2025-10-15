import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "").strip()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "").strip()
EMAIL_TO = os.getenv("EMAIL_TO", "").strip()

def _first_three_emails(raw):
    parts = [p.strip() for p in raw.replace(";", ",").split(",") if p.strip()]
    seen = set()
    out = []
    for p in parts:
        if p not in seen:
            seen.add(p)
            out.append(p)
        if len(out) == 3:
            break
    return out or ([EMAIL_ADDRESS] if EMAIL_ADDRESS else [])

def send_email(post_content):
    to_list = _first_three_emails(EMAIL_TO)

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("Email send failed: missing EMAIL_ADDRESS or EMAIL_PASSWORD")
        return False

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ", ".join(to_list)
        msg["Subject"] = "New LinkedIn Post Generated"
        msg.attach(MIMEText(post_content, "plain"))

        # Gmail SSL (App Password required)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return True
    except smtplib.SMTPAuthenticationError as e:
        print("Email auth failed:", e)
        print("Tip: Use Gmail App Password (2FA enabled) and verify EMAIL_ADDRESS/EMAIL_PASSWORD.")
        return False
    except Exception as e:
        print("Email send failed:", e)
        return False
