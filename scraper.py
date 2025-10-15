import requests
from bs4 import BeautifulSoup

URLS = [
    "https://www.sentinelone.com/cybersecurity-101/cybersecurity/cyber-security-trends/",
    "https://www.jpmorganchase.com/about/technology/blog/top-cybersecurity-trends-to-watch-in-2025",
    "https://thehackernews.com/",
    "https://www.darkreading.com/",
    "https://www.sans.org/blog",
    "https://www.cybersecuritydive.com/",
]

def fetch_articles(max_chars=20000, timeout=15):
    articles = []
    for url in URLS:
        try:
            r = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=timeout,
            )
            if r.status_code != 200:
                print(f"Non-200 for {url}: {r.status_code}")
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            text = " ".join(p.get_text(" ", strip=True) for p in soup.find_all("p"))
            text = text[:max_chars]
            if text:
                articles.append({"url": url, "content": text})
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
    return articles
