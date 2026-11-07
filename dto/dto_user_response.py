from typing import Literal
from pydantic import ConfigDict, Field
from pydantic import EmailStr
from typing import Optional
from pydantic import BaseModel
from role.role_enum import UserRole

class dto_user_response(BaseModel):
    id : Optional[str] = Field(default = None , alias = "_id")
    email : EmailStr
    role : UserRole
    model_config = ConfigDict(populate_by_name = True)