# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import kb_client

import os


bot = Bot(token=os.getenv('TOKEN'))
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'Привет! Я-бот It-cube. Хочешь познакомиться со мной и узнать об It-конкурсах? Скорее выбирай в меню интересующие кнопки и знакомься со мной ближе ', reply_markup=kb_client)

@dp.message_handler(commands=['Обо_мне'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'IT-cube - это центр цифрового образования детей по программам, направленным на ускоренное освоение актуальных и востребованных знаний, навыков и компетенций в сфере информационных технологий. Всё обучение в нашем центре проводится бесплатно.')


@dp.message_handler(commands=['ВК'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'https://vk.com/itcubenn')

@dp.message_handler(commands=['Местоположение'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'улица Генкиной, 84, Нижний Новгород')

@dp.message_handler(commands=['It-конкурсы'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'Фестиваль нейротехнологий-"Нейрофест"*https://www.научим.online/neuro-fest-2022')
	#await bot.send_message(message.from_user.id, ' Пригласительный этап в Сириусе*https://siriusolymp.ru/informatics')

@dp.message_handler(commands=['Сайт'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'https://itcube.nntc.nnov.ru/')

@dp.message_handler(commands=['Телефон'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, '+79915113881')


@dp.message_handler()
async def echo_send(message : types.Message):
	if message.text=='Привет' or message.text=='привет':

		await message.answer('И тебе привет! Введи /start, чтобы начать!')
	


executor.start_polling(dp, skip_updates=True)
