from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    user_id: int
    movie_id: int
    rating: float
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
