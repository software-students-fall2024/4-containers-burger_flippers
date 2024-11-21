import pytest
from unittest.mock import Mock
from web_app.app import app

#Test transcription
def test_transcribe(client, mock_file, mock_whisper, mock_db):
    """
    transcription of an audio file
    """
    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert "transcription" in response.json
    assert response.json["transcription"] == "This is a test"

# Test for missing file
def test_missing_file(client, mock_file, mock_whisper):
    """
    Test error handling when the file is not included in the request
    """
    data = {
        "file": None  # missing file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")

    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"] == "No file part"


# Test for successful transcription with mock whisper function
def test_transcribe_whisper_success(client, mock_file, mock_whisper, mock_db):
    """
    Test transcription success using the mocked whisper service
    """

    mock_whisper.transcribe.return_value = {"text": "Mocked transcription result"}

    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert "transcription" in response.json
    assert response.json["transcription"] == "Mock transcription result"

# Test failure when whisper service is unavailable
def test_transcribe_whisper_failure(client, mock_file, mock_whisper, mock_db):
    """
    Test error handling when whisper service fails
    """
    mock_whisper.transcribe.side_effect = Exception("Whisper service error")

    data = {
        "file": mock_file
    }
    response = client.post("/transcribe", data=data, content_type="multipart/form-data")

    assert response.status_code == 500
    assert "error" in response.json
    assert response.json["error"] == "Something is wrong with whisper, status code 500"
