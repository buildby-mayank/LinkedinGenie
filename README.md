LinkedinGenie — Auto‑curate, draft, and email LinkedIn posts from trusted sources

Overview
LinkedinGenie helps busy professionals publish consistent, high‑quality LinkedIn posts without the tab overload. It:

* Scrapes trusted sources
* Scores trending topics
* Drafts a human‑style post (no AI-y tone)
* Emails a ready‑to‑paste version to you

Quick start
Clone and install
Create and activate a virtual environment.
Install requirements:
pip install -r requirements.txt
Create .env (at project root)
Paste and fill the following (no quotes around values):

GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE

#Email configs
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_ADDRESS=your_gmail@gmail.com # sender address
EMAIL_PASSWORD=your_16_char_app_password # Gmail App Password (not your normal password)
EMAIL_TO=receiver1@example.com,receiver2@example.com

Notes:
Use a Gmail App Password (requires 2‑Step Verification). Do not use your normal Gmail password.
EMAIL_TO can be one or more comma‑separated emails. The script will send only to the first three.

Run
python main.py
Output: The script fetches articles, scores topics, generates a concise post, and emails it to the specified recipients.

What it does under the hood
Scraper: Pulls paragraph text from a small list of trusted URLs (adjustable).
Topic scoring: Consolidates text and asks Gemini to return a JSON map of topics → scores.
Drafting: Generates a succinct LinkedIn post with a hook, skimmable bullets, and a CTA.
Email: Sends the final post via authenticated SMTP.
Change the niche from “cyber + AI security” to anything
You can switch to any topic (finance, healthtech, devtools, marketing) by editing:

** modules/scraper.py
Replace URLS with your niche sources (blogs, journals, news portals, vendor reports, community hubs).
** modules/topic_scoring.py
Update the prompt’s criteria to reflect your domain. For example:
“Extract fintech topics” or “Extract frontend engineering trends”
Scoring can favor “developer impact,” “product adoption,” or “go‑to‑market relevance.”
** modules/post_generator.py
Adjust the style requirements and tone. For example: “Developer‑centric tips and code pointers” for engineering
“Market insights + customer outcomes” for product/marketing
Modify length, CTA, and any branding lines.

Tips for best results
Start with 5–8 high‑signal sources in your niche.
Keep the post length target under ~1500 characters to avoid “see more” fatigue.
Rotate sources and periodically prune low-signal feeds.
Never commit .env to version control; rotate keys if you suspect exposure.

Troubleshooting
Empty or auth errors: Ensure .env values are present, unquoted, and that an App Password is used.
Email blocked: Check Gmail security alerts; confirm STARTTLS on port 587 or switch to SSL 465 if preferred.
No topics found: Reduce scraped input size or add more targeted sources.
Too generic posts: Tighten scoring criteria and add style constraints in the drafting prompt.

License and attribution
Use responsibly. Respect site terms when scraping. Do not store or redistribute copyrighted content beyond fair use excerpts.
Credits to the original publishers of source articles; this project only paraphrases and links to public content.

Happy to share my code with you all !!!!
