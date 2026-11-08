from pydantic import EmailStr, Field
from pydantic import BaseModel

class dto_user_regist(BaseModel) :
    username : str
    email : EmailStr
    password : str = Field(min_length=8 , max_length=64)

class dto_user_login(BaseModel) :
    email : EmailStr
    password : str

class dto_user_update_password(BaseModel) :   
    old_password : str = Field(min_length=8 , max_length=64)
    new_password : str = Field(min_length=8 , max_length=64)
    confirm_password : str = Field(min_length=8 , max_length=64)
    

    
