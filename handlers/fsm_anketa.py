# import logging
# import aiogram.utils.markdown as md
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ParseMode, InputFile
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# # задаем логгирование
# logging.basicConfig(level=logging.INFO)
#
# # создаем бота и диспетчер
# bot = Bot(token="YOUR_TOKEN_HERE")
# dp = Dispatcher(bot, storage=MemoryStorage())
#
# # задаем состояния для вопросов
# class QuizQuestions(StatesGroup):
#     question_1 = State()
#     question_2 = State()
#     question_3 = State()
#     question_4 = State()
#     question_5 = State()
#     question_6 = State()
#     question_7 = State()
#     question_8 = State()
#     question_9 = State()
#     question_10 = State()
#
# # создаем клавиатуру с вариантами ответов для каждого вопроса
# def create_keyboard(question_number):
#     keyboard = InlineKeyboardMarkup()
#     if question_number == 1:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_1_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_1_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_1_3")
#         )
#     elif question_number == 2:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_2_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_2_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_2_3")
#         )
#     elif question_number == 3:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_3_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_3_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_3_3")
#         )
#     elif question_number == 4:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_4_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_4_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_4_3")
#         )
#     elif question_number == 5:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_5_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_5_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_5_3")
#         )
#     elif question_number == 6:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_6_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_6_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_6_3")
#         )
#     elif question_number == 7:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_7_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_7_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_7_3")
#         )
#     elif question_number == 8:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_8_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_8_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_8_3")
#         )
#     elif question_number == 9:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_9_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_9_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_9_3")
#         )
#     elif question_number == 10:
#         keyboard.add(
#             InlineKeyboardButton(text="Ответ 1", callback_data="question_10_1"),
#             InlineKeyboardButton(text="Ответ 2", callback_data="question_10_2"),
#             InlineKeyboardButton(text="Ответ 3", callback_data="question_10_3")
#         )
#     return keyboard
#
#
# questions = [
#     {"question": "Вопрос 1. Какой язык программирования вы предпочитаете?", "answer": ""},
#     {"question": "Вопрос 2. Какую операционную систему вы используете?", "answer": ""},
#     {"question": "Вопрос 3. Какую среду разработки вы предпочитаете?", "answer": ""},
#     {"question": "Вопрос 4. Какую базу данных вы чаще всего используете?", "answer": ""},
#     {"question": "Вопрос 5. Какую структуру данных вы предпочитаете?", "answer": ""},
#     {"question": "Вопрос 6. Какой фреймворк вы предпочитаете для веб-разработки?", "answer": ""},
#     {"question": "Вопрос 7. Какую библиотеку для машинного обучения вы используете?", "answer": ""},
#     {"question": "Вопрос 8. Какой формат данных вы предпочитаете для работы с текстами?", "answer": ""},
# ]
#
#
#
#
#
#
#
