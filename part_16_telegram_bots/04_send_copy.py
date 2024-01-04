import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6842779414:AAGLwf8lA5sOjdOsGousW58gtRZUuLuhLUA"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def answer_as_echo(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer("Unsupported media type...")


@dp.message()
async def reply_as_echo(message: types.Message):
    await message.reply(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
