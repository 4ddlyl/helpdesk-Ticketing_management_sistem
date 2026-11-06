from fastapi.security import OAuth2PasswordRequestForm

from utils.security import verify_access_token
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
def get_all_user(service_auth = Depends(ServiceAuth)):
    return service_auth.get_all_user()

@router_auth.post("/logout")
def user_logout(token : str = Depends(verify_access_token) , service_auth = Depends(ServiceAuth)):
    return service_auth.logout(token)

