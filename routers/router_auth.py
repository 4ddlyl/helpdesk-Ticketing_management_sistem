from services.service_auth import ServiceAuth
from fastapi import Depends
from dto.dto_user import dto_user_regist
from fastapi import APIRouter

router_auth = APIRouter(prefix= "/auth" , tags=["user"])

@router_auth.post("/auth/register")
def user_register(new_user : dto_user_regist , service_auth = Depends(ServiceAuth)) :
    return service_auth.regist_user(new_user)
