from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass  # no password

class UserResponse(UserBase):
    id: int
    # Make fields optional to tolerate existing NULLs in DB
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    email: Optional[EmailStr] = None
    # Pydantic v2 configuration for ORM serialization
    model_config = ConfigDict(from_attributes=True)
