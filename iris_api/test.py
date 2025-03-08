from fastapi.testclient import TestClient
from main import app  # Ensure 'main' is the filename where FastAPI app is defined

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
