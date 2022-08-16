from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types, executor
from main import dp, bot
from key_board import kb, kb2, kb3, kb4, kb5
from state import Nun_facts
from API_Num_facts import text_num
from translate import Translator
from BD2 import Database
translator = Translator(to_lang="ru")
db = Database("mysqlite.db")

@dp.message_handler(Command('Back'))
async def start_bot(message: types.Message):
    await message.answer("Меню", reply_markup=kb3)
@dp.message_handler(Command('Режимы'))
async def start_bot(message: types.Message):
    await message.answer("Выберите режим", reply_markup=kb)

@dp.message_handler(Command('start'))
async def start_bot(message: types.Message):
    r = db.get_users(message.from_user.id)
    if not len(r) == 0:
        pass
    else:
        db.add_user((message.from_user.id, message.from_user.first_name))
    await message.answer("Меню", reply_markup=kb3)
@dp.message_handler(Command('История_ваших_фактов'))
async def start_bot(message: types.Message):
    await message.answer("Меню истории фактов", reply_markup=kb5)

@dp.message_handler(Command('Очистить_историю'))
async def start_bot(message: types.Message):
    id_user = db.get_users(message.from_user.id)
    db.del_info(id_user[0][0])
    await message.answer("История очищена!!", reply_markup=kb3)

@dp.message_handler(Command("Итория"))
async def start_bot2(message:types.Message):
    id_user = db.get_users(message.from_user.id)
    result = db.show_all(id_user[0][0])
    print(result)
    if result == []:
        await message.answer(f'Вы нечего не вводили, история пустая',reply_markup=kb3)
    else:
        for i in result:
          await message.answer(f'Имя пользователя: {i[2]} \nТекст: {i[0]} \nТип текста: {i[1]}', reply_markup=kb4)

@dp.message_handler(Command('Факт_о_цифре'))
async def answer_q1(message: types.Message):
    await message.answer("Введите число")
    await Nun_facts.Q1.set()
@dp.message_handler(state=Nun_facts.Q1)
async  def state_1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(Q1=answer)
    dict_num = await state.get_data("Q1")
    num= dict_num['Q1']
    if not num.isdigit():
        await message.answer("Вы ввели не число")
    else:
        result = text_num("math", num)
        translation = translator.translate(result["text"])
        id_user = db.get_users(message.from_user.id)
        db.add_fact((id_user[0][0], result['text'], result["type"]))
        await message.answer(result["text"])
        await message.answer(f"Перевод текста: {translation}", reply_markup=kb2)
        await state.finish()
@dp.message_handler(Command('Факт_о_годе'))
async def answer_q2(message: types.Message):
    await message.answer("Введите число")
    await Nun_facts.Q2.set()
@dp.message_handler(state=Nun_facts.Q2)
async  def state_2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(Q2=answer)
    dict_num = await state.get_data("Q2")
    num= dict_num['Q2']
    if not num.isdigit():
        await message.answer("Вы ввели не число")
    else:
        result = text_num("year", num)
        translation = translator.translate(result["text"])
        id_user = db.get_users(message.from_user.id)
        db.add_fact((id_user[0][0], result['text'], result["type"]))
        await message.answer(result["text"])
        await message.answer(f"Перевод текста: {translation}", reply_markup=kb2)
        await state.finish()
@dp.message_handler(Command('Факт_о_жизни'))
async def answer_q3(message: types.Message):
    await message.answer("Введите число")
    await Nun_facts.Q3.set()
@dp.message_handler(state=Nun_facts.Q3)
async  def state_3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(Q3=answer)
    dict_num = await state.get_data("Q3")
    num= dict_num['Q3']
    if not num.isdigit():
        await message.answer("Вы ввели не число")
    else:
        result = text_num("trivia", num)
        translation = translator.translate(result["text"])
        id_user = db.get_users(message.from_user.id)
        db.add_fact((id_user[0][0], result['text'], result["type"]))
        await message.answer(result["text"])
        await message.answer(f"Перевод текста: {translation}", reply_markup=kb2)
        await state.finish()
@dp.message_handler(Command('Факт_о_дате'))
async def answer_q4(message: types.Message):
    await message.answer("Введите дату, в виде месяца и числа. Пример: 4 13, 4-месяц 13-день")
    await Nun_facts.Q4.set()
@dp.message_handler(state=Nun_facts.Q4)
async  def state_4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(Q4=answer)
    dict_num = await state.get_data("Q4")
    num= dict_num['Q4']
    print(len(num))
    if not len(num) >=3:
        await message.answer("Введите дату корректно")
    elif not num.replace(" ", "").isdigit():
        await message.answer("Вы ввели не число")
    else:
        print(num[2])
        if int(num[0]) >12 :
            await message.answer("Месяц или дата указана не верно")
        elif int(num[0]) <=0:
                await message.answer("Месяц или дата указана не верно")
        elif int(num[2:]) <=0:
                await message.answer("Месяц или дата указана не верно")
        elif int(num[2:]) >31 :
                await message.answer("Месяц или дата указана не верно")
        else:
                result = text_num("date", num.split(" "))
                translation = translator.translate(result["text"])
                id_user = db.get_users(message.from_user.id)
                db.add_fact((id_user[0][0], result['text'], result["type"]))
                await message.answer(result["text"])
                await message.answer(f"Перевод текста: {translation}", reply_markup=kb2)
                await state.finish()
@dp.message_handler(Command('Попробовать_еще'))
async def answer_q1(message: types.Message):
    await message.answer("Возврат к выбору факта", reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)