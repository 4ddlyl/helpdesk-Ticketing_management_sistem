from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class dto_message_response(BaseModel):
    id : Optional[str] = Field(default= None , alias= "_id")
    ticket_id : str
    sender_id : str
    sender_role : str
    message : str
    created_at : datetime