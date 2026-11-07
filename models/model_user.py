from bson import ObjectId
from pydantic import BaseModel, EmailStr
from pydantic import Field
from typing import Literal, Optional
from role.role_enum import UserRole

class Model_User_Regist(BaseModel) :
    id : Optional[str] = Field(default=None , alias="_id")
    username : str
    password : str
    email : Optional[EmailStr] = None
    role : UserRole = UserRole.CUSTOMER

    class Config :
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True    

class Model_User_Login(BaseModel):
    id : Optional[str] = Field(default=None , alias="_id")
    email : str
    password : str 

    class Config :
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True    
            


