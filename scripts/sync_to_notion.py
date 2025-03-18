import requests
import json
import os

# Load Notion API credentials
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

def get_latest_log():
    logs_dir = "logs"
    log_files = sorted(os.listdir(logs_dir), reverse=True)
    if not log_files:
        print("No logs found.")
        return None, None
    
    latest_log = log_files[0]
    with open(os.path.join(logs_dir, latest_log), "r") as file:
        log_content = file.read()
    
    return latest_log, log_content

def add_log_to_notion(title, content, github_link):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": title}}]},
            "Content": {"rich_text": [{"text": {"content": content}}]},
            "GitHub Link": {"url": github_link}
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    log_filename, log_content = get_latest_log()
    if log_filename:
        github_link = f"https://github.com/Melayu2020/Ai-Logs/new/main/logs/{log_filename}"
        notion_response = add_log_to_notion(log_filename, log_content, github_link)
        print("Synced to Notion:", notion_response)
