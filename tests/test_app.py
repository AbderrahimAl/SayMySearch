from fastapi.testclient import TestClient
from app.es_connection import client
from app.api import app

test_client = TestClient(app)

def test_es_conn():
    """Test elasticsearch connection"""

    assert client.ping()

def test_root():
    
    response = test_client.get("/")
    assert response.status_code == 200

def test_get_search():
    """Test search api"""

    
    response = test_client.get("/search?query=")
    assert response.status_code == 200