import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_BASE_URL='https://api.notion.com/v1'
NOTION_DATABASE_ID=os.getenv('NOTION_DATABASE_ID')
NOTION_HEADERS={
    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {os.getenv("NOTION_API_KEY")}',
    'content-type': 'application/json'
}

SLACK_API_BASE_URL='https://slack.com/api/chat.postMessage'