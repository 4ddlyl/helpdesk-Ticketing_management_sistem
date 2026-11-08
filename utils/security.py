import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from repositories.repo_auth import Repo_Auth
import jwt


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM ="HS256"

security_scheme = HTTPBearer()

def verify_access_token(credentials : HTTPAuthorizationCredentials = Depends(security_scheme)):
    token = credentials.credentials

    try :
        #for verification
        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])
        email : str = payload.get("sub")
        if email is None :
            raise HTTPException(401, "invalid token")
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(401 , "token sudah kadaluarsa , silahkan relog")
    except jwt.PyJWTError :
        raise HTTPException(401 , "gagal memverifikasi token")

def get_current_user(email :str = Depends(verify_access_token), repo : Repo_Auth = Depends(Repo_Auth)) :
    user = repo.find_by_email(email)
    if not user :
        HTTPException(401 , "not found")
    return user

def require_role(allowed_roles : list[str]):
    def role_checker(current_user = Depends(get_current_user)) :
        user_role = current_user.role
        if user_role not in allowed_roles :
            raise HTTPException(403 , f"akses ditolak  untuk role {user_role} , hanya {allowed_roles} yang di izinkan")
        return current_user
    return role_checker
    

      

