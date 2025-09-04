from aiogram import Router, Bot
from aiogram.types import Message
from config import FILES_CHANNEL
from database import save_file

router = Router()

@router.message()
async def save_user_file(message: Message, bot: Bot):
    file = None
    file_name = None
    file_size = None

    # Case 1: User uploads a file directly
    if message.document:
        file = message.document
        file_name = file.file_name
        file_size = file.file_size

    # Case 2: User forwards from another channel (check caption & media)
    elif message.video:
        file = message.video
        file_name = message.caption or "video.mp4"
        file_size = file.file_size

    elif message.audio:
        file = message.audio
        file_name = file.file_name
        file_size = file.file_size

    elif message.photo:
        # photos don’t have file_name → give default
        file = message.photo[-1]  # best quality
        file_name = message.caption or "photo.jpg"
        file_size = file.file_size

    else:
        return  # ignore text messages, stickers, etc.

    # Forward file to storage channel
    forwarded = await message.forward(FILES_CHANNEL)
    file_id = forwarded.message_id

    # Save in DB
    await save_file(file_id, file_name, file_size)

    # Confirm
    await message.answer(
        f"✅ Saved **{file_name}** ({round(file_size/1024/1024,2)} MB)\n\n"
        f"🔗 Link: `/get_{file_id}`",
        parse_mode="Markdown"
    )
