from typing import Optional
from pydantic import Field

class dto_category_create :
    name : str
    description : str

class dto_category_response :
    id : Optional[str] = Field(default=None ,alias="_id")
    name : str
    description : str
    