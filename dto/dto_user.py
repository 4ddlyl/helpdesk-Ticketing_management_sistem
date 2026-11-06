from pydantic import EmailStr
from pydantic import BaseModel

class dto_user_regist(BaseModel) :
    username : str
    email : EmailStr
    password : str

class dto_user_login(BaseModel) :
    email : EmailStr
    password : str
    

    
