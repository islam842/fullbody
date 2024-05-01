from config import dp
import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from Keyboards.client_kb import kbfinish, oneend


class TrainingStates(StatesGroup):
    SET_TRAINING_DURATIONN = State()
    SET_EXERCISE_DURATIONN = State()
    SET_REST_DURATIONN = State()
    END = State()


async def start(message: types.Message):
    await message.answer("Привет! Давай начнем тренировку. Сначала укажи общую длительность тренировки (в минутах)\n"
                         "\n"
                         "Учитывая отдых и время упражнений."
                         "Например: 120:")
    await TrainingStates.SET_TRAINING_DURATIONN.set()


@dp.message_handler(state=TrainingStates.SET_TRAINING_DURATIONN)
async def set_training_duration(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        training_duration = int(message.text)
        await state.update_data(training_duration=training_duration)
        await message.answer("Теперь укажи длительность упражнения (в минутах) Например: 3")
        await TrainingStates.SET_EXERCISE_DURATIONN.set()
    else:
        await message.answer("Пожалуйста введите в числах!")


@dp.message_handler(state=TrainingStates.SET_EXERCISE_DURATIONN)
async def set_exercise_duration(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        exercise_duration = int(message.text)
        await state.update_data(exercise_duration=exercise_duration)
        await message.answer("Теперь укажи длительность перерыва между упражнениями (в минутах) \n"
                             "Например: 3 \n"
                             "\n"
                             "Совет: Оптимальное время отдыха между подходами: 2-3 минут")
        await TrainingStates.SET_REST_DURATIONN.set()
    else:
        await message.answer("Пожалуйста введите в числах!")


@dp.message_handler(state=TrainingStates.SET_REST_DURATIONN)
async def set_rest_duration(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        rest_duration = int(message.text)
        async with state.proxy() as data:
            training_duration = data['training_duration']
            exercise_duration = data['exercise_duration']

        await message.answer(f"Прекрасно! Тренировка начинается.\n"
                             f"\n"
                             f"Общая длительность тренировки - ({training_duration}) минут,\n"
                             f"\n"
                             f"Упражнение будет длиться - ({exercise_duration}) минут,\n"
                             f"\n"
                             f"После чего будет перерыв в течение - ({rest_duration}) минут.\n")
        await asyncio.sleep(2)  # Задержка для подготовки пользователя
        await start_workout(message, training_duration, exercise_duration, rest_duration)
    else:
        await message.answer("Пожалуйста введите в числах!")


async def start_workout(message: types.Message, training_duration: int, exercise_duration: int, rest_duration: int):
    workout_time = training_duration
    while workout_time > 0:
        # Выполнение упражнения
        await message.answer(f"Тренировка началась! Осталось {workout_time} минут. "
                             f"Начинай упражнения! Время упражнения - {exercise_duration} минут.\n"
                             f"\n"
                             f"Отчёт пошёл!")
        await asyncio.sleep(exercise_duration * 60)  # Подождать указанное время упражнения
        workout_time -= exercise_duration

        if workout_time > 0:
            await message.answer(f"Отдых! Возьми небольшой перерыв {rest_duration} минут.")
            await asyncio.sleep(rest_duration * 60)
            workout_time -= exercise_duration  # Подождать указанное время отдыха

    # Завершение тренировки
    await message.answer("Тренировка завершена! Отличная работа!", reply_markup=kbfinish)
    await TrainingStates.END.set()


@dp.message_handler(state=TrainingStates.END)
async def end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "ЗАВЕРШИТЬ" or answer == "1":
        await message.answer("Тренировка завершена! Что бы вернуться в начало введи команду \n"
                             "(/start)")
        await state.finish()
    elif answer == "НАЧАТЬ С НАЧАЛА":
        await message.answer("Что бы начать с начала введи команду (/wefunc)")
        await state.finish()


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(start, commands=["wefunc"])