from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



b0=KeyboardButton('/Back')
b1= KeyboardButton('/Факт_о_цифре')
b2= KeyboardButton('/Факт_о_годе')
b3=KeyboardButton('/Факт_о_жизни')
b4=KeyboardButton('/Факт_о_дате')
b5=KeyboardButton('/Попробовать_еще')
b6=KeyboardButton('/История_ваших_фактов')
b7=KeyboardButton('/Режимы')
b8=KeyboardButton('/Итория')
b9=KeyboardButton('/Очистить_историю')

kb=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
kb.add(b6).insert(b1).add(b2).insert(b3).add(b4)

kb2=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
kb2.add(b5).insert(b6)


kb3=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
kb3.add(b7).insert(b6)

kb4=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
kb4.add(b0)

kb5=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
kb5.insert(b8).insert(b9)