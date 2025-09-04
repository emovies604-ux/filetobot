from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "👋 Welcome!\n\n"
        "📂 Send me any file and I’ll store it permanently.\n"
        "🔗 You’ll get a unique link to share & download anytime."
    )
