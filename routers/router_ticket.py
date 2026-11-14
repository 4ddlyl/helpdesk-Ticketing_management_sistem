from fastapi import APIRouter, Depends
from role.role_enum import UserRole
from utils.security import get_current_user
from services.service_ticket import Service_Ticket
from dto.tickets.dto_ticket import dto_ticket_create
from utils.security import require_role

router_ticket= APIRouter(prefix="/ticket" ,tags=["tiket"])

@router_ticket.post("/create")
def create_ticket(data : dto_ticket_create , current_user = Depends(get_current_user) , service_ticket = Depends(Service_Ticket) ,
                  user_Access = Depends(require_role([UserRole.CUSTOMER]))):
    return service_ticket.create_ticket(data , current_user.id)

@router_ticket.get("/tickets")
def get_all_tickets(service_tiket = Depends(Service_Ticket) , admin_only = Depends(require_role([UserRole.ADMIN]))):
    return service_tiket.get_all_ticket()

@router_ticket.get("/mytickets")
def get_my_tickets_router(customer_id : str ,service_tickets = Depends(Service_Ticket), 
                          user_access = Depends(require_role([UserRole.CUSTOMER]))):
    return service_tickets.get_my_tickets(customer_id)
