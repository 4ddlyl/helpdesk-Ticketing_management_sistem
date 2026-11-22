from fastapi import APIRouter, Depends
from dto.dto_rating_feedback import dto_rating_feedback
from role.role_enum import TicketStatus, UserRole
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

@router_ticket.get("/assigned")
def get_ticket_by_aggent_id(require_role = Depends(require_role([UserRole.AGENT])) , seervice_tickets = Depends(Service_Ticket)):
    return seervice_tickets.find_ticket_by_aggent(require_role.id)

@router_ticket.put("/{ticket_id}/assigned")
def update_status_ticket(ticket_id : str,agent_id : str, new_status : TicketStatus ,service_ticket = Depends(Service_Ticket),
                         user_access = Depends(require_role([UserRole.ADMIN]))):
    return service_ticket.update_status_ticket(ticket_id,agent_id ,new_status)

@router_ticket.put("/{ticket_id}/resolve")
def resolve_ticket(ticket_id : str , current_user = Depends(get_current_user) , service_ticket = Depends(Service_Ticket),
                   user_access = Depends(require_role([UserRole.AGENT]))):
    return service_ticket.resolve_ticket_by_agent(ticket_id ,current_user.id)

@router_ticket.put("/{ticket_id}/rating")
def rating_ticket(ticket_id : str , data : dto_rating_feedback , service_ticket = Depends(Service_Ticket) ,
                  current_user = Depends(get_current_user) , user_access = Depends(require_role([UserRole.CUSTOMER]))):
    return service_ticket.rating_and_feedback(ticket_id , data , current_user.id)

@router_ticket.get("/dashboard")
def get_admin_dashboard(service_ticket = Depends(Service_Ticket) , admin_only = Depends(require_role([UserRole.ADMIN]))):
    return service_ticket.get_dashboard()