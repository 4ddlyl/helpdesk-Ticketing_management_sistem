from typing import Optional
from pydantic import BaseModel, Field

class dto_category_create(BaseModel) :
    name : str
    description : str

class dto_category_response(BaseModel) :
    id : Optional[str] = Field(default=None ,alias="_id")
    name : str
    description : str
