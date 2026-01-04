from sqlalchemy.orm import Session
from models import HealthRecord

def create_health_record(db: Session, data, bmi, ai_advice):
    record = HealthRecord(
        calories=data.calories,
        sleep_hours=data.sleep_hours,
        weight=data.weight,
        height=data.height,
        bmi=bmi,
        ai_advice=ai_advice
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
