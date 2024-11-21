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

