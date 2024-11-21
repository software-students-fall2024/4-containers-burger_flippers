import os
import pytest
from io import BytesIO
from web_app.app import app, fs

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_file():
    file = BytesIO(b"fake audio content")
    file.filename = "test_audio.mp3"
    return file

def test_index_page(client):
    """
    Test GET request
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Upload Audio" in response.data 

def test_file_upload(client, mock_file):
    """
    Test POST request 
    """
    data = {
        "audio": (mock_file, "test_audio.mp3")
    }
    response = client.post("/", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File uploaded" in response.data

    file = fs.find_one({"filename": "test_audio.mp3"})
    assert file is not None
    assert file.filename == "test_audio.mp3"

def test_list_files(client, mock_file):
    """
    Test that files are listed correctly
    """

    data = {
        "audio": (mock_file, "test_audio.mp3")
    }

    client.post("/", data=data, content_type="multipart/form-data")
    
    response = client.get("/files")
    assert response.status_code == 200
    assert b"test_audio.mp3" in response.data  
