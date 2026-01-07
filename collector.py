"""
Read-only Reddit data collector for LLM evaluation.

- Uses official Reddit API (PRAW)
- No posting, voting, or messaging
- Public content only
"""

import praw
from typing import List, Dict


def get_reddit_client() -> praw.Reddit:
    return praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        username="YOUR_REDDIT_USERNAME",
        password="YOUR_REDDIT_PASSWORD",
        user_agent="python:reddit-llm-eval:v1.0 (by u/spicy-sparkes)",
    )


def fetch_qa_threads(
    subreddit_name: str,
    limit: int = 10,
) -> List[Dict]:
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    threads = []

    for submission in subreddit.hot(limit=limit):
        if submission.is_self and submission.num_comments > 5:
            submission.comments.replace_more(limit=0)

            threads.append(
                {
                    "subreddit": subreddit_name,
                    "title": submission.title,
                    "question": submission.selftext,
                    "answers": [
                        comment.body
                        for comment in submission.comments
                        if len(comment.body) > 50
                    ],
                }
            )

    return threads


if __name__ == "__main__":
    data = fetch_qa_threads("personalfinance", limit=5)

    for item in data:
        print("\n---")
        print("Q:", item["title"])
        print("Answers:", len(item["answers"]))
