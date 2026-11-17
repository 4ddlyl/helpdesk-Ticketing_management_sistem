from fastapi import APIRouter, Depends
from role.role_enum import UserRole
from utils.security import get_current_user, require_role
from services.service_message import Service_Message_ticket
from dto.messages.dto_message_create import dto_message_create

router_message_ticket = APIRouter(prefix="/messages" , tags=["ticket_messages"])

@router_message_ticket.post("/send/{ticket_id}")
def kirim_message(ticket_id : str ,data : dto_message_create , current_user = Depends(get_current_user), service_message = Depends(Service_Message_ticket),
                  usser_access = Depends(require_role([UserRole.CUSTOMER]))):
    return service_message.kirim_message(data,ticket_id,current_user.id,current_user.role.value)