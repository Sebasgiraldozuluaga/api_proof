from fastapi.testclient import TestClient
from main import app  # Importa la API

client = TestClient(app)

def test_suma():
    response = client.get("/suma?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 8}
