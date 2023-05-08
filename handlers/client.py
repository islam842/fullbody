# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
# from config import bot
# from aiogram import Dispatcher, types
# from database.bot_db import sql_command_random
# # from parser.new import parser
#
#
# async def quiz_command(message: types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     button = InlineKeyboardButton("NEXT", callback_data="button")
#     markup.add(button)
#
#     question = "В каком году были основаны курсы Geeks?"
#     answers = [
#         "2019",
#         "2018",
#         "2017",
#         "2020",
#     ]
#
#     await bot.send_poll(
#         chat_id=message.chat.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=1,
#         explanation="Раньше были курсы GeekTech потом был ренбрендинг и переименовали на Geeks",
#         open_period=15,
#         reply_markup=markup
#
#     )
#
#
# async def get_random_user(message: types.Message):
#     random_user = await sql_command_random()
#     await message.answer_photo(
#         caption=f"{random_user[2]} {random_user[3]} {random_user[4]} "
#                 f"{random_user[5]}\n@{random_user[1]}"
#     )
#
#
# async def get_news(message:types.Message):
#     news = parser()
#     for i in news:
#         await message.answer(
#             f"{i['link']}\n\n"
#             f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
#             f"{i['description']}\n"
#             f"{i['date_from_html']}\n",
#             parse_mode=ParseMode.HTML
#         )
#
#
# def register_handlers_client(dp: Dispatcher):
#     dp.register_message_handler(get_news, commands=['news'])
#     dp.register_message_handler(quiz_command, commands=['quiz'])
#     # dp.register_message_handler(get_random_user, commands=['get'])