from pydantic import BaseModel

class HealthInput(BaseModel):
    calories: int
    sleep_hours: float
    weight: float
    height: float
   
