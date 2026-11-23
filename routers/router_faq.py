from fastapi import APIRouter, Depends
from role.role_enum import UserRole
from utils.security import require_role
from services.service_faq import Service_Faq
from dto.dto_faq import create_dto_faq, response_dto_faq

router_faq = APIRouter(prefix= "/faq" , tags=["faqs"])

@router_faq.get("/all")
def get_all_faqs(service_faq = Depends(Service_Faq)):
    return service_faq.get_all_faqs_service()

@router_faq.post("/create", response_model=dict)
def create_faq(data : create_dto_faq , service_faq  = Depends(Service_Faq),
               admin_only = Depends(require_role([UserRole.ADMIN]))):
    return service_faq.create_faq_service(data)