import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, upload, get_file, search

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Register routers
dp.include_router(start.router)
dp.include_router(upload.router)
dp.include_router(get_file.router)
dp.include_router(search.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
