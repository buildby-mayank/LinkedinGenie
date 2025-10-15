from modules.scraper import fetch_articles
from modules.topic_scoring import score_topics
from modules.post_generator import generate_post
from modules.email_sender import send_email

def run_agent():
    print("Fetching articles...")
    articles = fetch_articles()
    if not articles:
        print("No articles fetched; aborting.")
        return

    print("Scoring topics using Gemini 2.5 Flash...")
    best_topics, all_topics = score_topics(articles)
    if not best_topics:
        print("No valid topics found.")
        return

    print("Generating LinkedIn post using Gemini 2.5 Flash...")
    post_content = generate_post(best_topics)
    if not post_content:
        print("No post content generated.")
        return

    print("Sending post via email...")
    ok = send_email(post_content)
    print("Done!" if ok else "Email failed.")

if __name__ == "__main__":
    run_agent()
