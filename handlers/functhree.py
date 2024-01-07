from config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from aiogram import types


class Quiz(StatesGroup):
    QUIZA = State()


async def start(message: types.Message):
    await message.answer("Привет, укажи ИМТ (индекс массы тела) \n"
                         "Который указал вам бот при получение программы тренировок.", reply_markup=healfunc)
    await Quiz.QUIZA.set()


@dp.message_handler(state=Quiz.QUIZA)
async def answer_quiz(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "Как делать жим лёжа?":
        await message.answer("1.Лягте на скамью так, чтобы ваши верхние спины и голова полностью касались ее поверхности.\n"
                             "\n"
                             "2.Ваши стопы должны быть крепко на земле для обеспечения стабильности.\n"
                             "\n"
                             "3.Положите лопатки на скамью, чтобы они были прочно прижаты.\n"
                             "Ваши глаза должны быть направлены вверх, и шея должна быть в естественной позиции.\n"
                             "\n"
                             "4.Возьмите гриф штанги чуть шире ширины плеч.\n"
                             "Руки должны быть прямыми и вертикальными относительно пола.\n"
                             "\n"
                             "Как показано ниже:")

    elif answer == "Как делать отжимания?":
        await message.answer("",reply_markup=submit_markup)
    elif answer == "Как делать присед?":
        await message.answer("",reply_markup=submit_markup)
    elif answer == "":
        await message.answer("",reply_markup=submit_markup)
    elif answer == "Чем полезен проект?":
        await message.answer("", reply_markup=submit_markup)
    elif answer == "МЕНЮ":
        await message.answer("Вы в меню, выберите команду.", reply_markup=b_markup)