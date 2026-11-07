from dto.dto_user_admin_and_aggent import dto_createstaff
from utils.security import require_role
from dto.dto_user_response import dto_user_response
from utils.security import verify_access_token,get_current_user
from services.service_auth import ServiceAuth
from fastapi import Depends
from dto.dto_user import dto_user_login, dto_user_regist
from fastapi import APIRouter

router_auth = APIRouter(prefix= "/auth" , tags=["user"])

@router_auth.post("/register")
def user_register(new_user : dto_user_regist , service_auth = Depends(ServiceAuth)):
    return service_auth.regist_user(new_user)

@router_auth.post("/login")
def user_login(input_user : dto_user_login , service_auth = Depends(ServiceAuth) ):
    return service_auth.login(input_user)

@router_auth.get("/users")
def get_all_user(service_auth = Depends(ServiceAuth) , admin_only = Depends(require_role(["admin"]))):
    return service_auth.get_all_user()

@router_auth.post("/logout")
def user_logout(token : str = Depends(verify_access_token) , service_auth = Depends(ServiceAuth)):
    return service_auth.logout(token)

@router_auth.get("/users/me" , response_model= dto_user_response)
def get_my_profil(mine = Depends(get_current_user)):
    return {
        "id" :mine.id,
        "email" : mine.email,
        "role" : mine.role
    }

@router_auth.post("/users/staff")
def create_staff(new_staff :dto_createstaff , service_auth = Depends(ServiceAuth), admin_only = Depends(require_role(["admin"]))) :
    return service_auth.create_staff(new_staff)
                 





