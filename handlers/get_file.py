from aiogram import Router, Bot
from aiogram.types import Message
from database import get_file
from config import FILES_CHANNEL

router = Router()

@router.message(lambda msg: msg.text and msg.text.startswith("/get_"))
async def get_file_cmd(message: Message, bot: Bot):
    file_id = message.text.split("_")[1]
    file_data = await get_file(file_id)

    if not file_data:
        return await message.answer("❌ File not found!")

    await bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=FILES_CHANNEL,
        message_id=int(file_id)
    )
