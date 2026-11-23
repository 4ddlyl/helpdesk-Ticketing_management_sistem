from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class Model_Faq(BaseModel):
    id : Optional[str] = Field(default=None ,alias="_id")
    question : str
    answer : str

    class Config :
        arbitary_types_allowed : True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name : True