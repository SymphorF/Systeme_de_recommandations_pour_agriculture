from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "Item": "Maize",
        "Area": "Albania",
        "Year": 2010,
        "average_rain_fall_mm_per_year": 1000.0,
        "avg_temp": 20.0,
        "Pesticide_use_total_tonnes": 500.0,
        "Fertilizer_Used": 0.5,
        "Irrigation_Used": 0.5,
        "Days_to_Harvest": 105.0
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "predicted_yield_hg_per_ha" in data
    assert isinstance(data["predicted_yield_hg_per_ha"], (int, float))


def test_recommend_endpoint():
    payload = {
        "Area": "Albania",
        "Year": 2010,
        "average_rain_fall_mm_per_year": 1000.0,
        "avg_temp": 20.0,
        "Pesticide_use_total_tonnes": 500.0,
        "Fertilizer_Used": 0.5,
        "Irrigation_Used": 0.5,
        "Days_to_Harvest": 105.0
    }

    response = client.post("/recommend", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "crop" in data[0]
    assert "predicted_yield_hg_per_ha" in data[0]
