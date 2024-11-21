"""
ML Client Script

This script connects to a MongoDB database and keeps the connection alive.
"""

import os
import datetime
import whisper
from flask import Flask,jsonify, request
import pymongo
from dotenv import load_dotenv

#load dotenv
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
flask_host = os.getenv("FLASK_HOST")
flask_port = int(os.getenv("FLASK_PORT"))

client = pymongo.MongoClient(mongo_uri)
db = client["transcriptions"]

#init flask
app = Flask(__name__)

#loading whisper model
print("loading whisper model...")
model = whisper.load_model("base")
print("whisper model sucessfully loaded!")

#receives user audio input, creates transcriptions, adds to database, and returns transcription to webapp
@app.route("/transcribe", methods=["POST"])
def transcribe():
    try:
        #receive user audio input
        file = request.files["file"]
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)

        #transcribing audio file
        print('transcribing new input...')
        result = model.transcribe(file_path)
        transcription = result["text"]
        print('transcribed')

        #saving transcription to database
        data = {
            "filename": file.filename,
            "transcription": transcription,
            "timestamp": datetime.datetime.now()
        }
        db["history"].insert_one(data)
        print("saved transcription to history")

        #return transcription
        return jsonify({"transcription": transcription}), 200

    except Exception as e:
        print("error transcribing")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print('connecting to mongodb database')
    try:
        app.run(host=flask_host, port=flask_port)
    except KeyboardInterrupt: #stop if received keyboard input
        print("detected interrupt-shutting down")
    finally:
        client.close()
