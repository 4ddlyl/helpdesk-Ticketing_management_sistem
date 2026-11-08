from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from role.role_enum import UserRole

class Model_User_Admin_And_Aggent(BaseModel) :
    id : Optional[str] = Field(default=None , alias="_id")
    username : str
    password :str
    role : UserRole

    class Config : 
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True
