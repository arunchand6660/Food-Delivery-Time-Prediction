from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
import joblib
import sklearn
import pandas as pd

model = joblib.load("delivary_time.pkl")

app = FastAPI(
    title="Delivery Prediction API"
)

class Delivery(BaseModel):
    Order_Hour: int
    Day_of_Week: str
    Is_Weekend: int
    Is_Festival: int
    Weather: str
    Pickup_Zone: str
    Dropoff_Zone: str
    Vehicle_Type: str
    Rider_Experience_Years: float
    Rider_Rating: float
    Restaurant_Rating: float
    Cuisine_Type: str
    Order_Items: int
    Restaurant_Load: str
    Preparation_Time_Min: int
    Road_Distance_km: float
    Delivery_Distance_Category: str
    Traffic_Level: str
    Number_of_Signals: int
    Average_Speed_kmph: float
    Delivery_Priority: str


# Open HTML frontend
@app.get("/")
def home():
    return FileResponse("templates/index.html")


# Prediction endpoint
@app.post("/predict")
def pred(data: Delivery):

    # Convert JSON input into DataFrame
    input_array = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_array)

    return {
        "Predicted Delivery Time": float(prediction[0])
    }