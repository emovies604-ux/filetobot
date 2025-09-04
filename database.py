import motor.motor_asyncio
import os
from config import MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["filetobot"]

async def save_file(file_id, name, size):
    await db.files.insert_one({
        "file_id": file_id,
        "name": name,
        "size": size
    })

async def get_file(file_id):
    return await db.files.find_one({"file_id": int(file_id)})

async def search_files(keyword):
    cursor = db.files.find({"name": {"$regex": keyword, "$options": "i"}})
    return await cursor.to_list(length=20)
