from config import dp
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from Keyboards.client_kb import healfunc, nabor, gived
import asyncio

class TrainingStates(StatesGroup):
    SET_TRAINING_DURATION = State()
    SET_EXERCISE_DURATION = State()
    SET_REST_DURATION = State()
    END = State()


async def start(message: types.Message):
    await message.answer("Привет, укажи ИМТ (индекс массы тела) \n"
                         "Который указал вам бот при получение программы тренировок.", reply_markup=healfunc)
    await TrainingStates.SET_TRAINING_DURATION.set()


@dp.message_handler(state=TrainingStates.SET_TRAINING_DURATION)
async def set_training_duration(message: types.Message, state: FSMContext):
    training_duration = message.text
    await state.update_data(training_duration=training_duration)
    await message.answer("Укажите свой вес(kg):\n"
                         "Например - 60")
    await TrainingStates.SET_EXERCISE_DURATION.set()


@dp.message_handler(state=TrainingStates.SET_EXERCISE_DURATION)
async def set_rest_duration(message: types.Message, state: FSMContext):
    rest_duration = message.text
    await state.update_data(rest_duration=rest_duration)
    if rest_duration.isdigit():
        await message.answer("Укажите что хотите: ", reply_markup=nabor)
        await TrainingStates.SET_REST_DURATION.set()
    else:
        await message.answer("Введите ваш вес!")
        await message.answer("Вы ввели некорректные данные! Введите команду (/start) что бы начать с начала.")
        await state.finish()


@dp.message_handler(state=TrainingStates.SET_REST_DURATION)
async def set_rest_duration(message: types.Message, state: FSMContext):
    exercise_duration = message.text
    await state.update_data(exercise_duration=exercise_duration)
    await message.answer("Обработка...")
    await asyncio.sleep(5)
    async with state.proxy() as data:
        training_duration = data['training_duration']
        rest_duration = data['rest_duration']

        weight = int(rest_duration) * 1.7
        weight = int(weight)
        fat = int(rest_duration) * 0.7
        fat = int(fat)
        carbohydrate = int(rest_duration) * 4
        carbohydrate = int(carbohydrate)

        norma = int(rest_duration) * 1.6
        norma = int(norma)
        fatnorma = int(rest_duration) * 0.6
        fatnorma = int(fatnorma)

    if exercise_duration == "НАБРАТЬ МАССУ" and training_duration == "НИЗКИЙ":
            await message.answer(f"Персональные распределение приемов пищи по вашим данным:\n"
                                 f"\n"
                                 f"-Ешьте каждые 3-4 часа для поддержания постоянного поступления питательных веществ.\n"
                                 f"\n"
                                 f"[Для набора массы - в день вам нужно употреблять]:\n"
                                 f"\n"
                                 f"      [{weight}]-Грамм Белка\n"
                                 f"\n"
                                 f"      [{fat}]-Грамм Жиров\n"
                                 f"\n"
                                 f"      [{carbohydrate}]-Грамм Углеводов\n"
                                 f"\n")
            await message.answer(f"Источники [БЕЛКА]: \n"
                                 f"Куриное мясо, индейка, рыба, яйца, молочные продукты, творог, бобы, гречка, орехи.\n"
                                 f"Распределение: включайте белки в каждый прием пищи.\n"
                                 f"\n"
                                 f"Источники [ЖИРА]\n"
                                 f"Источники: Оливковое масло, авокадо, орехи, лосось, семена чиа, льняные семена.\n"
                                 f"Избегайте насыщенных и трансжиров; употребляйте полиненасыщенные и мононенасыщенные "
                                 f"жиры.\n"
                                 f"\n"
                                 f"Источники [УГЛЕВОДА]:\n"
                                 f"Источники: Картошка, киноа, овсянка, фасоль, кукуруза, фрукты, овощи.\n"
                                 f"Приоритет углеводов до и после тренировок для поддержания энергии.")
            await message.answer("Введите команду (/start) для возращения в начало.")
            await state.finish()
    elif training_duration == "ИЗБИТОК":
        await message.answer(f"Персональные распределение приемов пищи по вашим данным:\n"
                                 f"\n"
                                 f"-Ешьте каждые 5-6 часа для поддержания постоянного поступления питательных "
                                 f"веществ.\n"
                                 f"\n"
                                 f"[Для набора массы и сушки - в день вам нужно употреблять]:\n"
                                 f"\n"
                                 f"      [{weight}]-Грамм Белка\n"
                                 f"\n"
                                 f"      [ДЕФИЦИТ]- Жиров\n"
                                 f"\n"
                                 f"      [ДЕФИЦИТ]- Углеводов\n"
                                 f"\n"
                                 f"Пейте достаточно воды: \n"
                                 f"Вода важна для обеспечения правильной гидратации, особенно во время физической "
                                 f"активности.\n"
                                 f"\n"
                                 f"Контролируйте углеводы и жиры: Распределите их так, чтобы соответствовать вашим "
                                 f"дневным потребностям, но с учетом калорийного дефицита.\n"
                                 f"\n"
                                 f"Источники здоровых жиров: Оливковое масло, авокадо, орехи, рыбий жир.")
        await message.answer(f"Источники [БЕЛКА]: \n"
                                 f"Куриное мясо, индейка, рыба, яйца, молочные продукты, творог, бобы, гречка, орехи.\n"
                                 f"Распределение: включайте белки в каждый прием пищи.\n"
                                 f"\n"
                                 f"")
        await message.answer("Введите команду (/start) для возращения в начало.")
        await state.finish()
    elif training_duration == "НОРМА":
        await message.answer(f"Персональные распределение приемов пищи по вашим данным:\n"
                                 f"\n"
                                 f"-Ешьте каждые 4 часа для поддержания постоянного поступления питательных веществ.\n"
                                 f"\n"
                                 f"[Для набора массы - в день вам нужно употреблять]:\n"
                                 f"\n"
                                 f"      [{norma}]-Грамм Белка\n"
                                 f"\n"
                                 f"      [{fatnorma}]-Грамм Жиров\n"
                                 f"\n"
                                 f"      [{carbohydrate}]-Грамм Углеводов\n"
                                 f"\n")
        await message.answer(f"Источники [БЕЛКА]: \n"
                                 f"Куриное мясо, индейка, рыба, яйца, молочные продукты, творог, бобы, гречка, орехи.\n"
                                 f"Распределение: включайте белки в каждый прием пищи.\n"
                                 f"\n"
                                 f"Источники [ЖИРА]\n"
                                 f"Источники: Оливковое масло, авокадо, орехи, лосось, семена чиа, льняные семена.\n"
                                 f"Избегайте насыщенных и трансжиров; употребляйте полиненасыщенные и мононенасыщенные "
                                 f"жиры.\n"
                                 f"\n"
                                 f"Источники [УГЛЕВОДА]:\n"
                                 f"Источники: Картошка, киноа, овсянка, фасоль, кукуруза, фрукты, овощи.\n"
                                 f"Приоритет углеводов до и после тренировок для поддержания энергии.")
        await message.answer("Введите команду (/start) для возращения в начало.")
        await state.finish()
    elif training_duration == "(СЛШ) ИЗБИТОК":
        await message.answer("Вам требуется обсудить персональное питание с вашим доктором!")
        await message.answer("Введите команду (/start) для возращения в начало.")
        await state.finish()

    else:
        await message.answer("Вы ввели некорректные данные! Введите команду (/start) что бы начать с начала.")
        await state.finish()


def register_handlers_extra1(dp: Dispatcher):
    dp.register_message_handler(start, commands=['healfunc'])