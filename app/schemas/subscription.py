from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional

class SubscriptionBase(BaseModel):
    plan_name: str
    price: float
    duration_days: int
    quality: Optional[str] = "HD"
    device_limit: Optional[int] = 1
    description: Optional[str] = None

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionResponse(SubscriptionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
