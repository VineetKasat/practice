# test_app.py
import app

def test_index():
    client = app.app.test_client()
    response = client.get('/')
    assert response.data == b'Hello from Podman!'

