import os
from pymongo import MongoClient
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()


MONGODB_USERNAME=os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD=os.getenv('MONGODB_PASSWORD')
MONGODB_ATLAS_INDEX_NAME=os.getenv('MONGODB_ATLAS_INDEX_NAME')
MONGODB_DATABASE_NAME=os.getenv('MONGODB_DATABASE_NAME')
MONGODB_COLLECTION_NAME=os.getenv('MONGODB_COLLECTION_NAME')

class MongoVectorDatabase:

    def __init__(self):
        MONGODB_DATABASE_URL=f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@notion-slack.jnssu0a.mongodb.net/'
        self.client = MongoClient(MONGODB_DATABASE_URL)
        self.db = self.client[MONGODB_DATABASE_NAME][MONGODB_COLLECTION_NAME]
        self.embedding = OpenAIEmbeddings()


    def delete(self, id):
        return self.db.delete_one(filter={ 'id': id })

    def add(self, task):
        embedded_task = self.embed(task)
        self.db.insert_one(embedded_task)

    def embed(self, task):
        text = f"""ID: {task['id']}
                Name: {task['properties']['Name']['title'][0]['text']['content'] if len(task['properties']['Name']['title']) > 0 else ''}
                description: {task['properties']['Description']['rich_text'][0]['text']['content'] if len(task['properties']['Description']['rich_text']) > 0 else ''}
                Priority: {task['properties']['Priority']['select']['name'] if task['properties']['Priority'] else ''}
                Status: {task['properties']['Status']['select']['name'] if task['properties']['Status'] else ''}
                Completion Date: {task['properties']['Creation Date']['created_time']}"""
        task["embedding"] = self.embedding.embed_query(text)
        task['text'] = text
        return task

    def delete_all(self):
        return self.db.delete_many({})

    def find_all(self):
        return self.db.find({})

mongo_db = MongoVectorDatabase()