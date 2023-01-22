from fastapi.testclient import TestClient
from app.es_connection import client
from app.api import app


def test_es_conn():
    """Test elasticsearch connection"""

    assert client.ping()


def test_get_search():
    """Test search api"""

    test_client = TestClient(app)
    response = test_client.get("/?query=")
    assert response.status_code == 200