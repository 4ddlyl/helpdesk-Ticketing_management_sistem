from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class Model_Message(BaseModel) :
    id : Optional[str] = Field(default=None, alias="_id")
    ticket_id : str
    sender_id : str
    sender_role : str
    message : str
    created_at : datetime = Field(default_factory=datetime.now)

    class Config:
        arbitary_types_allowed = True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True

