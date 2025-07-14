import os
import praw
from google import genai
from dotenv import load_dotenv

# 📥 Load environment variables
load_dotenv()

# ✅ Configure Gemini API
client = genai.Client()

# ✅ Configure Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def fetch_user_activity(reddit, username, post_limit=30, comment_limit=50):
    """
    Fetches recent posts and comments by the given Reddit username.
    """
    user = reddit.redditor(username)
    posts = list(user.submissions.new(limit=post_limit))
    comments = list(user.comments.new(limit=comment_limit))
    return posts, comments

def summarize_with_gemini(posts, comments):
    """
    Sends collected posts/comments to Gemini with a custom prompt
    to generate a cohesive user persona summary.
    """
    # Combine content for Gemini context
    snippets = []
    for p in posts:
        snippets.append(f"POST: {p.title}\n{p.selftext or ''}\n(URL: https://reddit.com{p.permalink})\n")
    for c in comments:
        snippets.append(f"COMMENT: {c.body}\n(URL: https://reddit.com{c.permalink})\n")
    combined = "\n\n".join(snippets[:20])  # Limit to avoid prompt size issues

    # 📝 Custom prompt
    prompt = f"""
You are an expert user researcher. 
Based on the following Reddit activity, generate a user persona including:
- Name (fictional or inferred from username)
- Motivations
- Personality traits
- Behaviors and habits
- Goals and needs
- Frustrations

For each point, include a short citation (with URL) from the posts/comments as evidence.

Reddit Activity:
{combined}
"""
    print("🔗 Sending data to Gemini for analysis...")
    
    response  = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text

def write_persona_to_file(persona_text, username):
    """
    Writes the LLM-generated user persona to a text file.
    """
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {filename}")

if __name__ == "__main__":
    profile_url = input("Enter Reddit profile URL: ").strip().rstrip("/")
    username = profile_url.split("/")[-1]

    # Step 1: Fetch Reddit data
    posts, comments = fetch_user_activity(reddit, username)

    # Step 2: Summarize via Gemini
    persona_text = summarize_with_gemini(posts, comments)

    # Step 3: Save output
    write_persona_to_file(persona_text, username)
