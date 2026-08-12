from aiogram import Router, F, types
from aiogram.filters import CommandStart
import groups

router = Router()

@router.message(CommandStart(), F.chat.type == "private")
async def cmd_start(message: types.Message):
    await message.answer("Привет! пришли свое сообщение.")

@router.message(F.chat.type == "private")
async def send_anon(message: types.Message):
    try:
        await message.copy_to(chat_id=groups.GROUP_ID)
        await message.answer("Отправлено")
    except Exception as e:
        await message.answer("Ошибка при отправке, попробуйте заново")