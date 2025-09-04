import os

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Database + Collection names
DB_NAME = os.getenv("DB_NAME", "filetobot")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "files")

# Files channel (must be your channel ID, like -1001234567890)
FILES_CHANNEL = int(os.getenv("FILES_CHANNEL", "-1002789851054"))
