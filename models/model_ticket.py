from typing import Optional
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from role.role_enum import TicketPriority, TicketStatus

class Model_Ticket(BaseModel) :
    id : Optional[str] = Field(default=None , alias="_id")
    ticket_number : Optional[str] = None
    title : str
    description : str
    category_id :Optional[str] = None
    priority : TicketPriority
    status : TicketStatus
    customer_id : Optional[str] = None
    agent_id : Optional[str] = None
    created_at : Optional[datetime] = None

    class Config :
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True

