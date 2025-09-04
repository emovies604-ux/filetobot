from aiogram import Router, F
from aiogram.types import Message
from database import save_file

router = Router()

@router.message(F.document)
async def handle_file(message: Message):
    file_id = message.document.file_id
    file_unique_id = message.document.file_unique_id
    file_name = message.document.file_name

    # Save with unique ID too
    await save_file(file_id, file_name)

    await message.answer(
        f"✅ File saved!\n\n"
        f"📂 Name: `{file_name}`\n"
        f"🔗 File ID: `{file_id}`\n"
        f"🆔 Unique ID: `{file_unique_id}`",
        parse_mode="Markdown"
    )
