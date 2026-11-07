from pydantic import BaseModel, EmailStr
from role.role_enum import UserRole

class dto_createstaff(BaseModel):
    username : str
    email : EmailStr
    password : str
    role : UserRole