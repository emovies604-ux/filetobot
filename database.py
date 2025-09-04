import motor.motor_asyncio
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def save_file(file_id: str, file_name: str, file_unique_id: str = None):
    """Save file details into MongoDB"""
    data = {"file_id": file_id, "file_name": file_name.lower()}
    if file_unique_id:
        data["file_unique_id"] = file_unique_id
    await collection.insert_one(data)

async def search_file(query: str):
    """Search for files by name (case-insensitive, regex)"""
    cursor = collection.find({"file_name": {"$regex": query.lower()}})
    return [doc async for doc in cursor]

async def get_file(file_unique_id: str):
    """Fetch a single file by its unique ID"""
    return await collection.find_one({"file_unique_id": file_unique_id})
