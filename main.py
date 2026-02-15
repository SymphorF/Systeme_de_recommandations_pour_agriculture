from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Charger le modèle
#model = joblib.load("model_xgb.pkl")
model_2 = joblib.load("model_rf_tt.pkl")

app = FastAPI(
    title="Crop Yield Prediction API",
    description="API de prédiction et recommandation de cultures",
    version="1.0"
)

# ----------------------------
# Schémas d'entrée
# ----------------------------

'''
class PredictInput(BaseModel):
    Item : str
    Area : str
    average_rain_fall_mm_per_year: float
    Pesticide_use_total_tonnes: float
    avg_temp: float

class RecommendInput(BaseModel):
    Area : str
    average_rain_fall_mm_per_year: float
    Pesticide_use_total_tonnes: float
    avg_temp: float
'''    


class PredictInput(BaseModel):
    Item : str
    Area : str
    Year: int
    average_rain_fall_mm_per_year: float
    avg_temp: float
    Pesticide_use_total_tonnes: float
    Fertilizer_Used: float
    Irrigation_Used: float
    Days_to_Harvest: float

class RecommendInput(BaseModel):
    Area : str
    Year: int
    average_rain_fall_mm_per_year: float
    avg_temp: float
    Pesticide_use_total_tonnes: float
    Fertilizer_Used: float
    Irrigation_Used: float
    Days_to_Harvest: float


# ----------------------------
# Endpoint 1 : Prédiction
# ----------------------------

@app.post("/predict")
def predict_yield(data: PredictInput):

    df = pd.DataFrame([data.dict()])

    prediction = model_2.predict(df)[0]

   #return {
   #    "predicted_yield_tons_per_hectare": round(float(prediction), 2)
   #}

    return {
        "predicted_yield_hg_per_ha": round(float(prediction), 2)
    }


# ----------------------------
# Endpoint 2 : Recommandation
# ----------------------------

@app.post("/recommend")
def recommend_crops(data: RecommendInput):

    crops = ['Maize', 'Rice', 'Soybean', 'Wheat']
    results = []

    for crop in crops:
        row = data.dict()
        row["Item"] = crop
        df = pd.DataFrame([row])

        pred = model_2.predict(df)[0]
        results.append({
            "crop": crop,
            #"predicted_yield": round(float(pred), 2)
            "predicted_yield_hg_per_ha": round(float(pred), 2)
        })

    results = sorted(results, key=lambda x: x["predicted_yield_hg_per_ha"], reverse=True)

    return results
