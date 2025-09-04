import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
FILES_CHANNEL = int(os.getenv("FILES_CHANNEL"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))  # optional
