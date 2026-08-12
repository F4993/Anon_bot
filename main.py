import asyncio
from aiogram import Bot, Dispatcher
import config
from handlers import router 

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    print("бот запущен ✨")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())