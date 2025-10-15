import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
client = genai.Client(api_key=GEMINI_API_KEY)

def score_topics(articles, max_input_chars=35000):
    combined_text = "\n\n".join(a.get("content", "") for a in articles)
    combined_text = combined_text[:max_input_chars]

    prompt = f"""
Extract cybersecurity and AI-security topics from the text below.

Scoring rules (0-100 per topic):
- Trending relevance (current, widely discussed)
- Novelty (specific, not evergreen)
- Pros/cons clarity (tradeoffs, risks visible)
- Real-world applicability (actionable impact)

Return ONLY a JSON object mapping topic name → integer score.
No commentary, no markdown.

Text:
{combined_text}
"""

    # Minimal signature for strict SDKs
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text_output = (response.text or "").strip()
    if not text_output:
        print("Empty response from Gemini.")
        return [], []

    # Robust JSON parse with fallback extraction
    try:
        topics_json = json.loads(text_output)
    except Exception:
        start = text_output.find("{")
        end = text_output.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                topics_json = json.loads(text_output[start:end + 1])
            except Exception as e:
                print("Failed to parse Gemini scoring:", e, "\nRaw:", text_output[:500])
                return [], []
        else:
            print("Failed to parse Gemini scoring: no JSON found\nRaw:", text_output[:500])
            return [], []

    clean = {}
    for k, v in topics_json.items():
        try:
            clean[str(k).strip()] = int(v)
        except Exception:
            continue

    sorted_topics = sorted(clean.items(), key=lambda x: (-x[1], x[0]))
    best_score = sorted_topics[0][1] if sorted_topics else 0
    best_topics = [t[0] for t in sorted_topics if t[1] == best_score]
    return best_topics, sorted_topics
