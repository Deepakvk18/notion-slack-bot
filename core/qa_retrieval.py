from pymongo import MongoClient
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import MongoDBAtlasVectorSearch
import pymongo
from core.database import mongo_db
from dotenv import load_dotenv

load_dotenv()

db = mongo_db.db

vector_search = MongoDBAtlasVectorSearch(
    collection=db,
    embedding=OpenAIEmbeddings(),
    # index_name=MONGODB_ATLAS_INDEX_NAME,
)
retriever = vector_search.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name='gpt-3.5-turbo'),
    chain_type="stuff",
    retriever=retriever,
)