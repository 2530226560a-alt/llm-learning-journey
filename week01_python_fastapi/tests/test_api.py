from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "LLM API Demo is running"


def test_chat():
    response = client.post(
        "/chat",
        json={
            "question": "什么是 RAG？",
            "user_id": "test_user",
            "temperature": 0.7
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "model" in data
    assert "tokens_used" in data