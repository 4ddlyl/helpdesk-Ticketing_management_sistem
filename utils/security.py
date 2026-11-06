import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
import jwt


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY_SECURITY")
ALGORITHM ="HS256"

security_scheme = HTTPBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_access_token(credentials : HTTPAuthorizationCredentials = Depends(security_scheme) , token : str=Depends(oauth2_scheme)):
    token = credentials.credentials

    try :
        #for verification
        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None :
            raise HTTPException(401, "invalid token")
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(401 , "token sudah kadaluarsa , silahkan relog")
    except jwt.PyJWTError :
        raise HTTPException(401 , "gagal memverifikasi token")            


