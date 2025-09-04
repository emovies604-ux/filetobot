from aiogram import Router
from aiogram.types import Message, FSInputFile
from database import search_file
from aiogram.filters import Command

router = Router()

@router.message(Command("search"))
async def search_cmd(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.answer("⚠️ Usage: `/search filename`", parse_mode="Markdown")

    query = parts[1].strip()
    results = await search_file(query)

    if not results:
        return await message.answer("❌ No files found!")

    # Limit results to 5 for readability
    for r in results[:5]:
        file_id = r["file_id"]
        file_name = r["file_name"]
        try:
            await message.answer_document(
                document=file_id,
                caption=f"📂 **{file_name}**",
                parse_mode="Markdown"
            )
        except Exception as e:
            await message.answer(f"⚠️ Couldn’t send `{file_name}` (maybe file expired).", parse_mode="Markdown")
