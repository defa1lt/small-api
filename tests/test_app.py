import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b"Hello, World!"

def test_get_data(client):
    rv = client.get('/api/data')
    assert rv.json == {"data": "Sample data"}

