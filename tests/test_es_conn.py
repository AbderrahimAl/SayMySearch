from app.es_connection import client

def test_conn():
    assert client.info()["tagline"] == "You Know, for Search"