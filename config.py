import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

TRUSTED_SITES = [
    "https://www.sentinelone.com/cybersecurity-101/cybersecurity/cyber-security-trends/",
    "https://www.jpmorganchase.com/about/technology/blog/top-cybersecurity-trends-to-watch-in-2025",
    "https://thehackernews.com/",
    "https://www.darkreading.com/",
    "https://www.sans.org/blog",
    "https://www.cybersecuritydive.com/",
]

EMAIL_CONFIG = {
    "host": "smtp.gmail.com",
    "port_ssl": 465,
    "port_starttls": 587,
    "user": os.getenv("EMAIL_ADDRESS", "").strip(),
    "password": os.getenv("EMAIL_PASSWORD", "").strip(),
    "to": os.getenv("EMAIL_TO", "").strip(),  # comma-separated
}
