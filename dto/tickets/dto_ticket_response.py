from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from role.role_enum import TicketPriority,TicketStatus

class dto_ticket_response(BaseModel) :
    id : Optional[str] = Field(default=None , alias="_id")
    ticket_number : str
    title : str
    status : TicketStatus
    priority : TicketPriority
    customer_id : Optional[str] = None
    agent_id : Optional[str] = None
    created_at : Optional[datetime] = None