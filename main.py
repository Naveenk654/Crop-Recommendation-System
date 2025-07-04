from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict, Any,Annotated
from pydantic import BaseModel, Field
import pandas as pd
import pickle
from crop_reason import crop_reasons  # Assuming you have a crop_reason module with the crop reasons
from weather import get_weather_data  # Assuming you have a weather module for fetching weather data
app= FastAPI()
with open('crop_prediction.pkl', 'rb') as f:
    model = pickle.load(f)
class UserInput(BaseModel):
    city: str = Field(..., description="City name for weather data")
    N: float = Field(..., description="Nitrogen content in soil")
    P: float = Field(..., description="Phosphorus content in soil")
    K: float = Field(..., description="Potassium content in soil")
    ph: float = Field(..., description="pH level of the soil")

@app.post("/predict")
def predict_crop(input_data: UserInput) :
    weather_data= get_weather_data(input_data.city)  
    input_df=pd.DataFrame({
        'N': [input_data.N],
        'P': [input_data.P],  
        'K': [input_data.K],
        'temperature': [weather_data['temperature']],
        'humidity': [weather_data['humidity']], 
        'ph': [input_data.ph],
        'rainfall': [weather_data['precipitation']]
    }) 
    prediction = model.predict(input_df)
    predicted_crop = prediction[0]  
    reason = crop_reasons.get(predicted_crop, "This crop suits your current weather and soil conditions.")
    return JSONResponse(content={"predicted_crop": predicted_crop,
                                 "why": reason})
