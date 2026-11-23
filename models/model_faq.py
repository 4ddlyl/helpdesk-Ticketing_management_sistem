from typing import Optional
from pydantic import BaseModel, Field

class Model_Faq(BaseModel):
    id : Optional[str] = Field(default=None ,alias="_id")
    question : str
    answer : str