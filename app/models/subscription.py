from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    duration_days = Column(Integer, nullable=False)
    quality = Column(String(50))      # e.g. "HD", "4K"
    device_limit = Column(Integer)
    description = Column(String(255))

    # Note: No relationship to User because there is no foreign key on users
