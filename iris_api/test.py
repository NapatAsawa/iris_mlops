from fastapi.testclient import TestClient
from main import app  # Ensure 'main' is the filename where FastAPI app is defined

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    # Define test input data
    test_data = {
        "data": [
            {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
            {"sepal_length": 6.7, "sepal_width": 3.1, "petal_length": 4.4, "petal_width": 1.4}
        ]
    }

    # Send POST request to /predict endpoint
    response = client.post("/predict", json=test_data)

    # Check if response is successful (HTTP 200)
    assert response.status_code == 200

    # Check if response has the correct structure
    json_response = response.json()
    assert "predictions" in json_response
    assert isinstance(json_response["predictions"], list)
    assert len(json_response["predictions"]) == len(test_data["data"])
