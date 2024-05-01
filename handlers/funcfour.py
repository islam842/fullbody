from config import dp
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
# from Keyboards.client_kb import
import asyncio


class TrainingStates(StatesGroup):
    SET_DO = State()
    SET_TO = State()
    SET_KG = State()
    SET_HEIG = State()
    END = State()



async def start(message: types.Message):
    await message.answer("Зравствуйте! Укажите сколько жмете и сколько хотите пожать.\n"
                         "Например жму 80кг хочу 100кг. \n"
                         "\n"
                         "Укажите сколько (кг) жмете например - 80")
    await TrainingStates.SET_TO.set()


@dp.message_handler(state=TrainingStates.SET_TO)
async def setto(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        setto = int(message.text)
        await state.update_data(setto=setto)
        await message.answer("Теперь укажи сколько (кг) хочешь пожать!\n"
                             "\n"
                             "Например - 100")
        await TrainingStates.SET_DO.set()
    else:
        await message.answer("Укажите в числах например - 80")

@dp.message_handler(state=TrainingStates.SET_DO)
async def setdo(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        setdo = int(message.text)
        await state.update_data(setdo=setdo)
        await message.answer("Теперь укажи свой вес в (кг).\n"
                             "\n"
                             "Например - 60")
        await TrainingStates.SET_KG.set()
    else:
        await message.answer("Укажите в числах например - 70")


@dp.message_handler(state=TrainingStates.SET_KG)
async def setkg(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        setkg = int(message.text)
        await state.update_data(setkg=setkg)
        await message.answer("Теперь укажи свой возраст.\n"
                             "\n"
                             "Например - 25")
        await TrainingStates.SET_HEIG.set()
    else:
        await message.answer("Укажите в числах например - 50")


@dp.message_handler(state=TrainingStates.SET_HEIG)
async def setheig(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        setheig = int(message.text)
        await message.answer("Обработка...")
        await asyncio.sleep(3)
        await state.update_data(setheig=setheig)
        async with state.proxy() as data:
            setto = data['setto']
            setdo = data['setdo']
            setkg = data['setkg']
            setheig = data['setheig']

        weight_diff = setdo - setto
        if setheig <= 20:
            if weight_diff <= 5:
                setkg1 = setto * 0.02 + setto
                await message.answer(f"Можешь добавить {setto * 0.02:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     "\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом жмем свой рабочий вес на:\n"
                                     f"-3-подхода по 10-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.02:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            elif 5 < weight_diff <= 10:
                setkg1 = setto * 0.03 + setto
                await message.answer(f"Можешь добавить {setto * 0.03:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     "\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом жмем свой рабочий вес на:\n"
                                     f"-3-подхода по 10-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.03:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            else:
                setkg1 = setto * 0.075 + setto
                await message.answer(f"Можешь добавить {setto * 0.075:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                    "\n"
                    f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                    f"\n"
                    f"Потом жмем свой рабочий вес на:\n"
                    f"-3-подхода по 12-14 повторений\n"
                    f"-Последний подход до отказа\n"
                    f"\n"
                    f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                    f"исправляя технику с помощью фукнции бота (truefunc).\n"
                    f"\n"
                    f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.075:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()

        elif 20 < setheig <= 30:
            if weight_diff <= 5:
                setkg1 = setto * 0.03 + setto
                await message.answer(f"Можешь добавить {setto * 0.03:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-3-подхода по 12-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее раз в месяц (раз в пол месяца) добавляя по {setto * 0.03:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            elif 5 < weight_diff <= 10:
                setkg1 = setto * 0.06 + setto
                await message.answer(f"Можешь добавить {setto * 0.06:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-3-подхода по 12-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.06:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            else:
                setkg1 = setto * 0.076 + setto
                await message.answer(f"Можешь добавить {setto * 0.076:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-3-подхода по 12-18 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее раз в неделюв месяц (раз в пол месяца) добавляя по {setto * 0.076:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
        elif 30 <= setheig:
            if weight_diff <= 5:
                setkg1 = setto * 0.04 + setto
                await message.answer(f"Можешь добавить {setto * 0.04:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-4-подхода по 12-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.04:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            elif 5 < weight_diff <= 10:
                setkg1 = setto * 0.07 + setto
                await message.answer(f"Можешь добавить {setto * 0.07:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-4-подхода по 12-16 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.07:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()
            else:
                setkg1 = setto * 0.080 + setto
                await message.answer(f"Можешь добавить {setto * 0.080:.2f}кг на текущий рекорд жима и попробуй пожать.\n"
                                     f"\n"
                                     f"Например на следущей тренировке попробуй пожать - {setkg1}кг\n"
                                     f"\n"
                                     f"Потом что бы увеличить жим. Жмем свой рабочий подход на:\n"
                                     f"-4-подхода по 12-18 повторений\n"
                                     f"-Последний подход до отказа\n"
                                     f"\n"
                                     f"Индивидуальный совет: практикуем жим своими рабочими весами всю неделю "
                                     f"исправляя технику с помощью фукнции бота (truefunc).\n"
                                     f"\n"
                                     f"Далее в месяц (раз в пол месяца) добавляя по {setto * 0.080:.2f}кг жмем свой максимум и достигем поставленной цели.")
                await message.answer("Проверяйте и каждые 1-2 недели заново проходим функцию - GYMFUNC")
                await message.answer("Введите команду (/start) для возращения в начало.")
                await state.finish()

    else:
        await message.answer("Укажите в числах например - 50")
def register_handlers_extras(dp: Dispatcher):
    dp.register_message_handler(start, commands=["gymfunc"])


