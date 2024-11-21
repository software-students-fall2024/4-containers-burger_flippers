"""
Web app for uploading audio files and storing them in MongoDB.
"""

import os
from flask import Flask, render_template, request
import pymongo
import gridfs

app = Flask(__name__)

# mongodb
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = pymongo.MongoClient(mongo_uri)
db = client["sensor_data"]
fs = gridfs.GridFS(db)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Route to display the upload form and handle audio uploads.
    """
    if request.method == "POST":
        file = request.files.get("audio")
        if file and file.filename:
            fs.put(file, filename=file.filename)
            return list_files()

    return render_template("index.html")


@app.route("/files")
def list_files():
    """
    Route to list all stored audio files and their transcriptions.
    """
    # Get transcriptions from the history collection
    transcriptions = list(db["history"].find().sort("timestamp", -1))
    return render_template("files.html", transcriptions=transcriptions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT", "5001")))
