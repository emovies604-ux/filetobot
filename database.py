import motor.motor_asyncio
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def save_file(file_id: str, file_name: str):
    """Save file details into MongoDB"""
    await collection.insert_one({"file_id": file_id, "file_name": file_name.lower()})

async def search_file(query: str):
    """Search for files by name (case-insensitive, regex)"""
    cursor = collection.find({"file_name": {"$regex": query.lower()}})
    return [doc async for doc in cursor]
