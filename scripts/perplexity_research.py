import os
import requests
import json

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

def fetch_research():
    # Simulated API request to Perplexity (Replace with actual API call)
    research_result = "Perplexity Research: Latest trends in AI automation suggest hybrid human-AI collaboration is the future."

    notion_payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": "Perplexity AI Research"}}]},
            "Content": {"rich_text": [{"text": {"content": research_result}}]}
        }
    }

    notion_headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=notion_headers, data=json.dumps(notion_payload))
    print("Notion Sync Response:", response.json())

if __name__ == "__main__":
    fetch_research()
