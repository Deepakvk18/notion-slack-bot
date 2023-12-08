import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

NOTION_API_KEY=os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID=os.getenv('NOTION_DATABASE_ID')
NOTION_PAGE_ID=os.getenv('NOTION_PAGE_ID')
NOTION_BASE_URL='https://api.notion.com/v1'
NOTION_BOT_USERID=os.getenv('NOTION_BOT_USERID')

class NotionClient():

    def __init__(self):
        self.headers = {
            'Notion-Version': '2022-06-28',
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.request = requests.Session()
        self.request.headers = self.headers

    def create_database(self, new_database):
        response = self.request.post(f'{NOTION_BASE_URL}/databases', new_database)
        return response.json()

    def update_database(self, updated_database):
        print(updated_database)
        response = self.request.post(f'{NOTION_BASE_URL}/databases/{updated_database.get("database_id")}', json.dumps(updated_database))
        return response.json()

    def retrieve_database(self, database_id):
        response = self.request.get(f'{NOTION_BASE_URL}/databases/{database_id}')
        return response.json()

    def query_database(self, database_id):
        response = self.request.post(f'{NOTION_BASE_URL}/databases/{database_id}/query')
        return response.json()

    def create_page(self, new_page):
        response = self.request.post(f'{NOTION_BASE_URL}/pages', json.dumps(new_page))
        return response.json()

    def update_page(self, page_id, updated_page):
        response = self.request.patch(f'{NOTION_BASE_URL}/pages/{page_id}', json.dumps(updated_page))
        return response.json()

    def retrieve_page(self, page_id):
        response = self.request.get(f'{NOTION_BASE_URL}/pages/{page_id}')
        return response.json()

    def archive_page(self, page_id):
        response = self.request.patch(f'{NOTION_BASE_URL}/pages/{page_id}', json.dumps({'archived': 'true'}))
        return response

    def create_block(self, new_block):
        response = self.request.post(f'{NOTION_BASE_URL}/blocks', new_block)
        return response.json()

    def update_block(self, block_id, updated_block):
        response = self.request.patch(f'{NOTION_BASE_URL}/blocks/{block_id}', updated_block)
        return response.json()

    def retrieve_block(self, block_id):
        response = self.request.get(f'{NOTION_BASE_URL}/pages/{block_id}')
        return response.json()

    def retrieve_user(self, user_id):
        response = self.request.get(f'{NOTION_BASE_URL}/users/{user_id}')

    def list_users(self):
        response = self.request.get(f'{NOTION_BASE_URL}/users')
        return response.json()

    def me(self):
        response = self.request.get(f'{NOTION_BASE_URL}/users/me')
        return response.json()
    
notion_client = NotionClient()