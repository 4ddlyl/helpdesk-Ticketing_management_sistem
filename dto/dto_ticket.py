from pydantic import BaseModel
from role.role_enum import TicketPriority

class dto_ticket_create(BaseModel) :
    title : str
    description : str
    category_id : str
    priority : TicketPriority = TicketPriority.MEDIUM    
