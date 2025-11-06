import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

def get_mongo_client():
    try:
        client = MongoClient(MONGO_URI)
        client.server_info()  # test de connexion
        print("Connected to MongoDB")
        return client
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        raise
