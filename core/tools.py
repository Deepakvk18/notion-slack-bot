from langchain.tools import tool
from core.schema import FindDocSchema, CreatePageSchema, UpdatePageSchema, SamplePageCreate, SamplePageUpdate
from core.database import mongo_db
from core.service import notion_client
from core.qa_retrieval import qa

@tool(args_schema=FindDocSchema)
def get_tasks(query: str):
    """This function can be used to get the tasks list"""
    return qa(query)

@tool(args_schema=FindDocSchema)
def find_related_doc(query: str):
    """This function can be used to retrieve the IDs of the task which the user is searching about"""
    return qa(f'ID of the task relating to this statement "{query}"')['result']

@tool(args_schema=CreatePageSchema)
def create_page(new_page: SamplePageCreate):
    """
    This function is used when the user needs to create a new notion task
    """
    new_page = notion_client.create_page(new_page)
    mongo_db.add(new_page)
    return None

@tool(args_schema=UpdatePageSchema)
def update_page(page_id: str, updated_page: SamplePageUpdate):
    """This function is used when the user needs to update the notion task.
    """
    updated_page = SamplePageUpdate(**updated_page).dict(exclude_none=True)
    updated_page = notion_client.update_page(page_id, updated_page)
    mongo_db.delete({'id': page_id})
    mongo_db.add(updated_page)

tools = [update_page, create_page, find_related_doc, get_tasks]