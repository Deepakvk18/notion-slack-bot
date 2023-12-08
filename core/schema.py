from pydantic.v1 import BaseModel, Field
from typing import List, Optional

class Text(BaseModel):
    content: str

class TextContent(BaseModel):
    text: Text

class Title(BaseModel):
    title: List[TextContent]

class RichTextContent(BaseModel):
    text: Text

class RichText(BaseModel):
    rich_text: List[RichTextContent]

class SelectItem(BaseModel):
    name: str

class SelectProperty(BaseModel):
    select: SelectItem

class DateObject(BaseModel):
    start: str = Field(description="Date in form 2023-11-27T11:27:00.000Z")

class DateProperty(BaseModel):
    date: DateObject

class PageProperties(BaseModel):
    Name: Optional[Title]
    Related_Articles: Optional[RichText]
    Status: Optional[SelectProperty]
    Expected_Completion_Date: Optional[DateProperty]
    Description: Optional[RichText]
    Priority: Optional[SelectProperty]

class CreatePageProperties(BaseModel):
    Name: Title
    Related_Articles: RichText
    Status: SelectProperty
    Expected_Completion_Date: DateProperty
    Description: RichText
    Priority: SelectProperty

class Parent(BaseModel):
    database_id: str

class SamplePageCreate(BaseModel):
    parent: Parent
    properties: CreatePageProperties

class SamplePageUpdate(BaseModel):
    properties: PageProperties

class UpdatePageSchema(BaseModel):
    page_id: str = Field(description="Page id of the page to be updated")
    updated_page: SamplePageUpdate = Field(description="Page object with updated details")

class CreatePageSchema(BaseModel):
    new_page: SamplePageCreate = Field(description="New Page object with all the required details")

class DeletePageSchema(BaseModel):
    page_id: str = Field(description="Page id of the page to be deleted")

class FindDocSchema(BaseModel):
    query: str = Field(description="Complete Query String of the user")