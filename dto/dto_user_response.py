from typing import Literal
from pydantic import Field
from pydantic import EmailStr
from typing import Optional
from pydantic import BaseModel

class dto_user_response(BaseModel):
    id : Optional[str] = Field(default = None , alias = "_id")
    email : EmailStr
    role : Literal ["customer" , "admin" , "agent"] = "customer"