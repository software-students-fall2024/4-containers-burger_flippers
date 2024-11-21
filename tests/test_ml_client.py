import pytest
from unittest.mock import Mock
from werkzeug.datastructures import FileStorage
from io import BytesIO

@pytest.fixture
def mock_file():
    # Mocking a file upload with FileStorage
    file = BytesIO(b"fake audio data")  # Simulating file content
    file.filename = 'test_audio.wav'
    file.content_type = 'audio/wav'
    return FileStorage(file)

@pytest.fixture
def mock_whisper():
    whisper = Mock()
    return whisper

@pytest.fixture
def mock_db():
    db = Mock()
    return db

def test_transcribe(client, mock_file, mock_whisper, mock_db):
    """
    Test successful transcription of an audio file
    """
    # Mock the whisper service to return a mock transcription result
    mock_whisper.transcribe.return_value = {"text": "Mocked transcription result"}

    # Simulate the file data being sent to the endpoint
    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")

    # Assert response code and expected result
    assert response.status_code == 200
    assert "Mocked transcription result" in response.data.decode()

def test_transcribe_file_not_found(client, mock_file, mock_whisper):
    """
    Test error handling when the file is not included in the request
    """
    data = {
        "file": None  # Simulate missing file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")
    
    # Assert the response status code and error message
    assert response.status_code == 400
    assert "No file provided" in response.data.decode()

def test_transcribe_db_error(client, mock_file, mock_whisper, mock_db):
    """
    Test handling of a database error during the transcription process
    """
    # Simulate a database error
    mock_db.insert_one.side_effect = Exception("Database error")
    
    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")
    
    # Assert the response status code and error message
    assert response.status_code == 500
    assert "Database error" in response.data.decode()

def test_transcribe_whisper_success(client, mock_file, mock_whisper, mock_db):
    """
    Test transcription success using the mocked whisper service
    """
    # Set up the mock to return the expected transcription result
    mock_whisper.transcribe.return_value = {"text": "Mocked transcription result"}
    
    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")
    
    # Assert the response status code and expected result
    assert response.status_code == 200
    assert "Mocked transcription result" in response.data.decode()

def test_transcribe_whisper_failure(client, mock_file, mock_whisper, mock_db):
    """
    Test error handling when whisper service fails
    """
    # Simulate whisper service failure by raising an exception
    mock_whisper.transcribe.side_effect = Exception("Whisper service error")
    
    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")
    
    # Assert the response status code and error message
    assert response.status_code == 500
    assert "Whisper service error" in response.data.decode()
