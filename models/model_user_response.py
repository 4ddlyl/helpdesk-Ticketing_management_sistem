from pydantic import EmailStr
from pydantic import Field
from typing import Optional

class Model_user_Response :
    id : Optional[str] = Field(default=None , alias="_id")
    email : EmailStr
    role : str