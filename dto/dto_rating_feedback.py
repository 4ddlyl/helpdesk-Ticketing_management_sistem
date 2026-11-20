from pydantic import BaseModel, Field

class dto_rating_feedback(BaseModel):
    rating : int = Field(ge=1 ,le=5)
    ulasan : str