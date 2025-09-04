from aiogram import Router, Bot
from aiogram.types import Message
from config import FILES_CHANNEL
from database import save_file

router = Router()

@router.message(lambda msg: msg.document)
async def save_user_file(message: Message, bot: Bot):
    file = message.document
    # Forward file to storage channel
    forwarded = await message.forward(FILES_CHANNEL)
    file_id = forwarded.message_id

    await save_file(file_id, file.file_name, file.file_size)

    await message.answer(
        f"✅ Saved **{file.file_name}** ({round(file.file_size/1024,2)} KB)\n\n"
        f"🔗 Link: `/get_{file_id}`",
        parse_mode="Markdown"
    )
