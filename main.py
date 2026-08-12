import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
import config
from handlers import router 

# Указываем прокси для PythonAnywhere
session = AiohttpSession(proxy="http://proxy.server:3128")

bot = Bot(token=config.BOT_TOKEN, session=session)
dp = Dispatcher()

dp.include_router(router)

async def main():
    print("бот запущен ✨")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
