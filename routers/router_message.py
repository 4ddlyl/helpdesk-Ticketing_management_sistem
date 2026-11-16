from fastapi import APIRouter, Depends
from services.service_message import Service_Message_ticket
from dto.messages.dto_message_create import dto_message_create

router_message_ticket = APIRouter(prefix="/messages" , tags=["ticket_messages"])

@router_message_ticket.post("/send/{ticket_id}")
def kirim_message(ticket_id : str ,data : dto_message_create , service_message = Depends(Service_Message_ticket)):
    return service_message.kirim_message(data,ticket_id)