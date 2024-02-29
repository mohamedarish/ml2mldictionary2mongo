import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

DATABASE_NAME = os.getenv("MONGO_DB")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION")

password = os.getenv("password")

uri = f"mongodb+srv://malo:{password}@cluster0.x1jcief.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(
    uri,
    server_api=ServerApi("1"),
)

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

with open("dictionary/dictionary.json", "r", encoding="utf-8-sig") as file:
    data = json.load(file)

for item in data:
    if "id" in item:
        del item["id"]

results = collection.insert_many(data)

print(f"Inserted {len(results.inserted_ids)} documents into the collection:")
print(results.inserted_ids)
