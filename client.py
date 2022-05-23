from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1= KeyboardButton('/Обо_мне')
b2= KeyboardButton('/ВК')
b3= KeyboardButton('/Местоположение')
b4= KeyboardButton('/It-конкурсы')
b5= KeyboardButton('/Сайт')
b6= KeyboardButton('/Телефон')

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)