from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram import Router
import hashlib

router = Router()

@router.inline_query()
async def inline_query(inquery: InlineQuery):
    query = inquery.query.strip()
    if not query:
        return
    try:
        result = eval(query, {"__builtins__": {}}, {})
        result_text = f"{query} = {result}"
    except Exception:
        result_text = "Invalid math expression."
    result_id = hashlib.md5(query.encode()).hexdigest()

    item = InlineQueryResultArticle(
        id=result_id,
        title="Click to send the result",
        description=result_text,
        input_message_content=InputTextMessageContent(message_text=result_text),
    )
    await inquery.answer([item], cache_time=1)

