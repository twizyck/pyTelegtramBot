import asyncio
from gc import callbacks
from math import lgamma

from telebot.apihelper import answer_web_app_query
from telebot.async_telebot import AsyncTeleBot
from telebot.callback_data import CallbackData
from telebot.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    ReplyKeyboardMarkup
import telebot
from telebot import types
import asyncio
import random
from datetime import datetime

bot = AsyncTeleBot('8095372914:AAF4gyURPVtt31r1dIinA-ROTHtRi23P2hw')

async def init_bot():
    await bot.set_my_commands([
        BotCommand('start', 'Запусти бата ага'),
    ])

#Inline-кнопки
inline_markup = types.InlineKeyboardMarkup()
inline_markup.add(types.InlineKeyboardButton("узнать дату сегодня браттт", callback_data="get_date"))
inline_markup.add(types.InlineKeyboardButton("случайна числа палучить", callback_data="get_random"))
inline_markup.add(types.InlineKeyboardButton("мем палучить", callback_data="get_meme"))

# Обычная клавиатура
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add("О боте", "Помощь")

#список мемов тут корчое
meme_files = [
    "bombardiro.png",
    "crocodilo.png",
    "gusino.png"
]

#обработчики
#обработка старта и выбора действие
@bot.message_handler(commands=['start'])
async def handle_any(message: Message):
    await bot.send_message(message.chat.id,'Салам алейкум брат.\n'
                                           'тут ты можешь всё\n'
                                           )

    await bot.send_message(message.chat.id, "выбери действиа брааааттт:", reply_markup=inline_markup)

#обработчик кнопок
@bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call):
    if call.data == "get_date":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await bot.send_message(call.message.chat.id, f"сягодня за окном: {now}")

    elif call.data == "get_random":
        num = random.randint(1, 100)
        await bot.send_message(call.message.chat.id, f"случайна числа: {num}")

    elif call.data == "get_meme":
        meme_path = random.choice(meme_files)
        with open(meme_path, "rb") as meme:
            await bot.send_photo(call.message.chat.id, meme)


async def main():
    await init_bot()
    await bot.polling()

if __name__ == '__main__':
    asyncio.run(main())