from typing import Optional
from pydantic import BaseModel, Field

class create_dto_faq(BaseModel):
    question : str
    answer : str

class response_dto_faq(BaseModel):
    id : Optional[str] = None
    question : str
    answer : str    
