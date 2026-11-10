from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field
from role.role_enum import TicketPriority, TicketStatus

class Model_Tickets(BaseModel) :
    id : Optional["str"] = Field(default=None , alias="_id")
    ticket_number : str
    title : str
    description : str
    category_id :str
    priority : TicketPriority
    status : TicketStatus
    customer_id : str
    aggent_id : Optional[str] = None

    class Config :
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True

