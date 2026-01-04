from fastapi import FastAPI
from schemas import HealthInput
from rules import rule_analysis
from ai_advisor import get_ai_advice 
#----for MYSQL Database------
from database import SessionLocal, engine
from models import Base
from crud import create_health_record
#----------frontend----------
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
#this for database operation to connect database
Base.metadata.create_all(bind=engine)
# frontend logic



origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"message": "NCD Intelligent Agent Backend Running"}



@app.post("/analyze")
def analyze(data: HealthInput):
    db = SessionLocal()

    rules_result = rule_analysis(data)
    ai_result = get_ai_advice(data)

    height_m = data.height / 100 #cm calculation
    bmi = data.weight / (height_m * height_m)


    create_health_record(db, data, bmi, ai_result)

    db.close()

    return {
        "rule_based_analysis": rules_result,
        "ai_advice": ai_result
    }
    

    #this endpoint is for progress
