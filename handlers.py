from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BufferedInputFile
from image_generator import create_card
import groups

router = Router()

def get_card_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сделать картинку", callback_data="make_photo")]
    ])

@router.message(CommandStart(), F.chat.type == "private")
async def cmd_start(message: types.Message):
    await message.answer("Привет! пришли свое сообщение")

@router.message(F.chat.type == "private", F.text)
async def send_anon(message: types.Message):
    try:
        await message.bot.send_message(
            chat_id=groups.GROUP_ID,
            text=f"<b>Новое анонимное сообщение:</b>\n\n{message.text}",
            parse_mode="HTML",
            reply_markup=get_card_keyboard()
        )
        await message.answer("Отправлено")
    except Exception as e:
        print(e)
        await message.answer("Ошибка при отправке")

@router.callback_query(F.data == "make_photo")
async def handle_make_photo(callback: types.CallbackQuery):
    text = callback.message.text or callback.message.caption or ""
    clean_text = text.replace("Новое анонимное сообщение:\n\n", "").strip()
    
    if not clean_text:
        await callback.answer("Не удалось прочитать текст", show_alert=True)
        return

    await callback.answer("Генерирую картинку...")

    try:
        photo_bytes = create_card(clean_text)
        photo = BufferedInputFile(photo_bytes.read(), filename="question.png")
        
        await callback.message.reply_photo(photo=photo)
    except Exception as e:
        print(e)
        await callback.message.reply("Ошибка при генерации фото")
