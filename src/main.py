from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI()
model_pipeline = joblib.load("/app/models/RandomForest_model.joblib")  # Path to your saved model pipeline
class InferenceData(BaseModel):
    Age: int
    LengthOfStay: int
    AR_DRG: str
    Principal_ProcedureCode: str
    CareType: str
    SourceOfReferral: str
    UrgencyOfAdmission: str
    AgeGroup: str
    WeekendStay: int
    Sex: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Machine Learning Model API!"}

@app.post("/predict")
def predict(data: InferenceData):
    try:
        input_data = pd.DataFrame([data.dict()])
        input_data = input_data.rename(columns={'AR_DRG': 'AR-DRG'})
        prediction = model_pipeline.predict(input_data)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))