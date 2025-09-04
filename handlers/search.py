from aiogram import Router
from aiogram.types import Message
from database import search_files

router = Router()

@router.message(lambda msg: msg.text and msg.text.startswith("/search"))
async def search_cmd(message: Message):
    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.answer("⚠️ Usage: `/search filename`", parse_mode="Markdown")

    keyword = query[1]
    results = await search_files(keyword)

    if not results:
        return await message.answer("❌ No files found!")

    text = "🔎 **Search Results:**\n\n"
    for f in results[:10]:  # limit 10 results
        text += f"📄 {f['name']} — /get_{f['file_id']}\n"

    await message.answer(text, parse_mode="Markdown")
