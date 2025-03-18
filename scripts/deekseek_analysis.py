import os
import requests
import json

# Load API keys from GitHub Secrets
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

def analyze_logs():
    # Simulated analysis - replace with DeepSeek API call
    analysis_result = "DeepSeek Analysis: Most common AI question is 'How to automate tasks?'"  

    # Send result to Notion
    notion_payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": "DeepSeek AI Analysis"}}]},
            "Content": {"rich_text": [{"text": {"content": analysis_result}}]}
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
    analyze_logs()
