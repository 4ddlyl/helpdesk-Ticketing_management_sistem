from bson import ObjectId
from pydantic import EmailStr
from pydantic import Field
from typing import Literal, Optional

class Model_user_Response :
    id : Optional[str] = Field(default=None , alias="_id")
    email : EmailStr

    class Config :
        arbitary_types_allowed =True
        json_encoders = {ObjectId : str}
        allow_population_by_field_name = True