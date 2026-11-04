from bson import ObjectId
from pydantic import EmailStr
from pydantic import Field
from typing import Optional

class Model_User_Regist :
    id : Optional[str] = Field(default=None , alias="_id")
    username : str
    password : str
    email : Optional[EmailStr] = None

    class Config :
        arbitery_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True

class Model_User_Login :
    id : Optional[str] = Field(default=None , alias="_id")
    email : str
    password : str 

    class Config :
        arbitery_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True
