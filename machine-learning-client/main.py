"""
Accepts user audio input, creates a transcription, and sends it back to the webapp client
"""

import os
import datetime
import whisper
from flask import Flask, jsonify, request
import pymongo
from dotenv import load_dotenv

# load dotenv
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
flask_host = os.getenv("FLASK_HOST")
flask_port = int(os.getenv("FLASK_PORT"))

client = pymongo.MongoClient(mongo_uri)
db = client["sensor_data"]

# init flask
app = Flask(__name__)

# loading whisper model
print("loading whisper model...")
model = whisper.load_model("base")
print("whisper model sucessfully loaded!")


# receives user audio input, creates transcriptions, adds to database
# and returns transcription to webapp
@app.route("/transcribe", methods=["POST"])
def transcribe():
    """
    Handle transcription requests by processing an audio file,
    saving the transcription to the database, and returning the result.
    """
    try:
        # receive user audio input, saving it to tmp folder
        file = request.files["file"]
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)
        # to test audio:
        # test_file_name = "test.mp3"
        # test_file_path = "./tmp/test.mp3"

        # transcribing audio file
        print("transcribing new input...")
        result = model.transcribe(file_path)
        transcription = result["text"]
        print("transcribed")

        # saving transcription to database
        data = {
            "filename": file.name,
            "transcription": transcription,
            "timestamp": datetime.datetime.now(),
        }
        db["history"].insert_one(data)
        print("saved transcription to history")

        # return transcription
        return jsonify({"transcription": transcription}), 200

    except FileNotFoundError as e:
        print(f"File error: {e}")
        return jsonify({"error": "File not found"}), 400
    except pymongo.errors.PyMongoError as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500


if __name__ == "__main__":
    print("connecting to mongodb database")
    try:
        app.run(host=flask_host, port=flask_port)
    except KeyboardInterrupt:
        print("detected interrupt-shutting down")
    finally:
        client.close()
