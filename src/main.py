import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("MONGO_DB")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION")

client = MongoClient()

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
