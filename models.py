from sqlalchemy import Column, Integer, Float, String,DateTime
from database import Base
from sqlalchemy.sql import func

class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    calories = Column(Integer)
    sleep_hours = Column(Float)
    weight = Column(Float)
    height = Column(Float)
    bmi = Column(Float)
    ai_advice = Column(String(2000))

    # This is for timestamp in database
    created_at = Column(DateTime(timezone=True), server_default=func.now())
