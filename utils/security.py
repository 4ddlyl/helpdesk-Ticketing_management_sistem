import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
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

