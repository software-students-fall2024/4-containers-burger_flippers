# In tests/test_mocks.py

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_file():
    file = Mock()
    file.filename = "test_audio.mp3"
    return file

@pytest.fixture
def mock_whisper():
    whisper = Mock()
    whisper.transcribe.return_value = {"text": "This is a test transcription."}
    return whisper

@pytest.fixture
def mock_db():
    db = Mock()
    db.insert_one.return_value = {"filename": "test_audio.mp3", "text": "This is a test transcription."}
    return db
