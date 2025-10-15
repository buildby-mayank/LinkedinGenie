import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_post(topics, max_chars=1500):
    topics_line = ", ".join(topics)
    prompt = f"""
Write a professional, human-style LinkedIn post (no AI tone, no emojis) about:
{topics_line}

Requirements:
- Bold-style hook line
- Skimmable bullets or short paragraphs
- Clear takeaways for practitioners
- Light attribution cue (e.g., “recent coverage from trusted sources”)
- An engaging CTA inviting practitioner perspectives
- Under {max_chars} characters total
- No plagiarism; paraphrase ideas only

Return only the post text.
"""

    # Minimal signature for strict SDKs
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    post_text = (response.text or "").strip()
    if len(post_text) > max_chars:
        post_text = post_text[: max_chars - 1].rstrip() + "…"
    return post_text
