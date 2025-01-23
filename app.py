from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault

from config import BOT_TOKEN
import asyncio

from handlers import router

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

async def startup(tg: Bot):
    await tg.set_my_commands(commands=[
        BotCommand(command="start", description="Botni ishga tushurish"),
        BotCommand(command="help", description="Yordam olish"),
    ], language_code='uz', scope=BotCommandScopeDefault())


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())