# -*- coding: utf-8 -*-

import configparser
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

config = configparser.ConfigParser()
config.read("config.ini")

bot = Bot(token=config["production"]["token"])
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(True, True)
keyboard.row("Комунікативна установка")
keyboard.row("Прив\'язаність до близьких")
keyboard.row("Емоційні перешкоди в спілкуванні")

keyboard2 = InlineKeyboardMarkup()
keyboard2.add(InlineKeyboardButton('Діагностика комунікативної установки', callback_data='button1'))
keyboard2.add(InlineKeyboardButton('Опитувальник прив\'язаності до близьких людей', callback_data='button2'))
keyboard2.add(InlineKeyboardButton('Емоційні перешкоди в міжособистісному спілкуванні', callback_data='button3'))

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    text = open('text/start.txt', 'r').read().format(
    first_name=message.from_user.first_name,
    last_name=message.from_user.last_name)
    await bot.send_message(message.from_user.id, text , reply_markup=keyboard2)

@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    text = message.from_user.first_name + " " + message.from_user.last_name
    await bot.send_message(config["production"]["admin_id"], text)
    await bot.send_message(config["production"]["admin_id"], message.from_user.id)
    await bot.send_message(config["production"]["admin_id"], message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
