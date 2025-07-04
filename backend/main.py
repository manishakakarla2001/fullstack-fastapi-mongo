from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import os 

app = FastAPI()

# CORS (so frontend JS can call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup
# Use environment variable for MongoDB URI
mongo_uri = os.getenv("MONGODB_URI", "mongodb://root:example@localhost:27017")
client = MongoClient(mongo_uri)
db = client["crud_app"]
collection = db["items"]

# Pydantic model
class Item(BaseModel):
    name: str
    description: str

# Routes
@app.post("/items/")
def create_item(item: Item):
    result = collection.insert_one(item.dict())
    return {"id": str(result.inserted_id), **item.dict()}

@app.get("/items/", response_model=List[Item])
def get_items():
    items = list(collection.find())
    return [{"name": i["name"], "description": i["description"]} for i in items]
