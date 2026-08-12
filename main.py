import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import BotCommand
import config
from handlers import router 

session = AiohttpSession(proxy="http://proxy.server:3128")
bot = Bot(token=config.BOT_TOKEN, session=session)
dp = Dispatcher()

dp.include_router(router)

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота")
    ])
    print("bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
