from config import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from Keyboards.client_kb import answer_markup, give, ans_markup, pro, pro1, instruc, givegym, submit_markup, givetrue, cancel_markup, active_markup, mot_markup, an_markup, a_markup, b_markup, FUNC, func_markup
import asyncio
import random
from handlers.functwo import register_handlers_extra  # Импортируем функции из вашего файла handlers
from handlers.funcone import register_handlers_extra1  # Импортируем функции из вашего файла handlers
from handlers.functhree import register_handlers_extraa  # Импортируем функции из вашего файла handlers
from handlers.funcfour import register_handlers_extras
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# logging.basicConfig(level=logging.INFO)
# register_handlers_extra1(dp)
# register_handlers_extraa(dp)
# register_handlers_extras(dp)


class Test(StatesGroup):
    Q1 = State()  # Состояние для первого вопроса
    Q2 = State()  # Состояние для второго вопроса
    Q3 = State()  # Состояние для третьего вопроса
    Q4 = State()  # Состояние для четвертого вопроса
    Q5 = State()  # Состояние для пятого вопроса
    Q6 = State()  # Состояние для шестого вопроса
    Q7 = State()  # Состояние для седьмого вопроса
    Q8 = State()  # Состояние для восьмого вопроса
    Q9 = State()
    random = State()
    END = State()
    Q10 = State()
    FUNC1 = State()
    FUNC2 = State()
    MENU = State()
    QUIZ = State()
    ENDFUNC = State()
    PRO = State()
    PRO1 = State()



@dp.message_handler(commands=['start'])
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    with open('Untitled 50.png', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer('Добро пожаловать в уникальный Телеграмм бот для тренировок и набора массы!\n'
                         '\n'
                         'FULLBODY(BETA)- Ваш персональный тренер!'
                         '\n'
                         'Наш бот адаптируется к вашим потребностям, учитывая ваше:\n'
                         '\n'
                         '-Тело\n'
                         '-Вес\n'
                         '-Рост\n'
                         '-Поцент жира\n'
                         '-Ваш ИМТ\n'
                         '\n'
                         'Получайте персональные планы тренировок на ближайшую неделю, а также возможность выполнять '
                         'упражнения вместе с ботом с правильной техникой и получить консультацию о питании.\n'
                         '\n'
                         'Наша главная задача - помочь вам достичь ваших целей. Готовы начать?', reply_markup=ans_markup)
    await Test.Q2.set()  # Переход ко второму вопросу


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'НАЧАТЬ!':
        await message.answer("Подпишитесь на наши каналы:\n"
                             "\n"
                             "Официальный телеграм канал - https://t.me/fullbodyproject \n"
                             "Официальный инстаграм аккаунт - \n")
        await message.answer("секунду...")
        delay_seconds = 6
        await asyncio.sleep(delay_seconds)
        await message.answer("Как вас зовут?")
        await Test.Q3.set()  # Переход к третьему вопросу
    elif answer == "О НАС":
        with open('Untitled (9).png', 'rb') as photo:
            # Отправляем фото в чат
            await message.answer_photo(photo)
        await message.answer("Добро пожаловать в мир FULLBODY! Мы - стартап-проект, созданный с любовью к здоровью "
                             "и фитнесу. \n"
                             "\n"
                             "Наша цель - помочь вам достичь своих тренировочных целей и набрать массу.\n"
                             "\n"
                             "С нашей помощью вы сможете улучшить свою физическую форму и достичь лучших "
                             "результатов. \n"
                             "Давайте вместе преобразим ваше тело и жизнь!\n"
                             "\n"
                             "С помощью наших функций вы практически получите личного тренера!\n"
                             "\n"
                             "Телеграмм канал проекта - https://t.me/fullbodyproject\n"
                             "ТикТок аккаунт проекта - \n"
                             "Инстаграмм аккаунт проекта - \n"
                             "FULL-PHONK-BODY музыка фонки - https://t.me/full_phonk_body", reply_markup=answer_markup)
    elif answer == "ХОЧУ ЗАДАТЬ ВОПРОС":
        await message.answer("Выберите вопрос который хотите задать?", reply_markup=submit_markup)
        await Test.QUIZ.set()
    elif answer == "ПОЛНАЯ-ПРО ВЕРСИЯ":
        await message.answer("FULLBODY-PRO - Более 10+ уникальных, персональных функций и отличий!\n", reply_markup=pro1)
        await Test.PRO.set()
    elif answer == "МЕНЮ":
        await message.answer("Вы в меню выберите команду:", reply_markup=b_markup)
        await Test.MENU.set()
    elif answer == "ФУНКЦИИ БОТА":
        await message.answer("ВЫБЕРИТЕ ФУНКЦИЮ", reply_markup=func_markup)
        await Test.FUNC1.set()
    elif answer == "ПОДДЕРЖАТЬ ПРОЕКТ":
        await message.answer("Спасибо за обращение!\n"
                             "Обратитесь создателям проекта: @theiws")
        await message.answer("Вы в меню выберите команду:",reply_markup=b_markup)
        await Test.MENU.set()
    else:
        await message.answer("Выберите команду!")


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isalpha():
        await state.update_data(q2=answer)  # Сохранение ответа на второй вопрос
        data = await state.get_data()  # Получение всех ответов
        q2 = data.get('q2')
        name = q2
        await message.answer(f'Отлично {name}, Ваш рост? (см)')
        await Test.Q4.set()  # Переход к пятому вопросу
    else:
        await message.answer("Пожалуйста введите ваше имя!")


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        await state.update_data(q3=answer)  # Сохранение ответа на третий вопрос
        await message.answer('Очень хорошо! Ваш возраст?')
        await Test.Q5.set()  # Переход к пятому вопросу
    else:
        await message.answer("Пожалуйста введите ваш рост!")


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        await state.update_data(q4=answer)  # Сохранение ответа на четвертый вопрос
        await message.answer('Отлично! Ваш вес? (кг)\n')
        await Test.Q6.set()  # Переход к пятому вопросу
    else:
        await message.answer("Пожалуйста введите ваш возраст!")


@dp.message_handler(state=Test.Q6)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isdigit():
        await state.update_data(q5=answer)  #
        await message.answer("Ваш образ жизни?\n"
                             "(Сидячий)\n"
                             "(Умеренный)\n"
                             "(Активный)", reply_markup=active_markup)
        await Test.Q7.set()
    else:
        await message.answer("Введите ваш вес!")


@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer.isalpha():
        await state.update_data(q6=answer)  # Сохранение ответа на пятый вопрос
        await message.answer("Ваш уровень мотивации?\n"
                             "\n"
                             "Низкое(Могу пропустить пару тренировок из-за настроении.)\n"
                             "\n"
                             "Среднее(Могу регулярно ходить и не пропускать тренировки.)\n"
                             "\n"
                             "Хорошая(Не пропускаю тренировки, дисциплинированный.)", reply_markup=mot_markup)
        await Test.Q8.set()
    else:
        await message.answer("Введите команду (/start) что бы начать заново.")
        await state.finish()


@dp.message_handler(state=Test.Q8)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    await state.update_data(q7=answer)
    if answer.isalpha():
        data = await state.get_data()
        q3 = data.get('q3')
        q4 = data.get('q4')
        q5 = data.get('q5')
        await message.answer('Всё верно? \n'
                             f'\nВаш рост: {q3}см\n'
                             f'\nВаш возраст: {q4}\n'
                             f'\n'
                             f'Ваш вес: {q5}кг', reply_markup=cancel_markup)
        await Test.Q9.set()
    else:
        await message.answer("Пожалуйста введите ваш вес!")


@dp.message_handler(state=Test.Q9)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "Да":
        await state.update_data(q8=answer)  # Сохранение ответа на пятый вопрос
        await message.answer("Обработка ваших данных....")
        delay_seconds = 5
        await asyncio.sleep(delay_seconds)
        await message.answer("Обработка прошла успешно! Получить подробный план?", reply_markup=cancel_markup)
        await Test.END.set()
    else:
        await message.answer("Введите команду (/start) что бы начать заново.")
        await state.finish()


@dp.message_handler(state=Test.QUIZ)
async def answer_quiz(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "Что такое спортпитание?":
        await message.answer("Спортпитание - это особый вид питания и добавок, который помогает спортсменам улучшить "
                             "свои результаты в тренировках, спортивных соревнованиях "
                             "и восстановиться после них.",reply_markup=submit_markup)
    elif answer == "Что такое тренировки?":
        await message.answer("Тренировки - это физические упражнения и занятия, проводимые с целью улучшения "
                             "физической "
                             "формы, развития навыков или достижения спортивных целей.",reply_markup=submit_markup)
    elif answer == "Как быстро могу набрать массу?":
        await message.answer("Чтобы быстро набрать массу, нужно сосредоточиться на трех ключевых факторах:\n"
                             "1.Питание: Увеличьте прием калорий, увеличивая потребление белков, углеводов и здоровых "
                             "жиров.\n"
                             "2.Тренировки: Сосредоточьтесь на силовых тренировках, чтобы стимулировать рост мышц.\n"
                             "3.Восстановление: Обеспечьте организм достаточным сном и отдыхом, чтобы мышцы могли "
                             "восстанавливаться и расти.\n"
                             "Однако помните, что набор массы требует времени и усилий, и важно выполнять это процесс"
                             " здорово и уравновешенно, под контролем специалиста, если возможно.",reply_markup=submit_markup)
    elif answer == "Сколько времени стабильно нужно уделять?":
        await message.answer("Чтобы стабильно набирать массу, рекомендуется тренироваться примерно 3-5 раз в неделю.\n"
                             " Это позволит вам обеспечить достаточный стимул для роста мышц и прогресса в вашей цели"
                             " набора массы",reply_markup=submit_markup)
    elif answer == "Чем полезен проект?":
        await message.answer("Наш Телеграмм-бот - идеальное решение для тренировок и набора мышечной массы.\n"
                             "-Он уникален, так как адаптируется к вашему телу, весу, росту и проценту жира,\n"
                             "-предоставляя индивидуальные планы тренировок на неделю.\n"
                             "-Мы также предоставляем возможность совместных упражнений,\n"
                             "обеспечивая оптимальное время отдыха и максимальный прогресс.\n"
                             "-В будущем, мы также добавим режимы для похудения и достижения конкретных целей, делая"
                             " нашего бота многофункциональным помощником в вашей тренировке!", reply_markup=submit_markup)
    elif answer == "МЕНЮ":
        await message.answer("Вы в меню, выберите команду.", reply_markup=b_markup)
        await Test.MENU.set()
    else:
        await message.answer("Пожалуйста выберите вопрос!")


@dp.message_handler(state=Test.MENU)
async def menu(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "ХОЧУ ЗАДАТЬ ВОПРОС":
        await message.answer("Выберите вопрос который хотите задать?", reply_markup=submit_markup)
        await Test.QUIZ.set()
    elif answer == "НАЧАТЬ!":
        await message.answer("Погрузись в мир - <FULLBODY>", reply_markup=an_markup)
        await Test.Q2.set()
    elif answer == "О НАС":
        await message.answer("Погрузись в мир - <FULLBODY>", reply_markup=a_markup)
        await Test.Q2.set()
    elif answer == "ФУНКЦИИ БОТА":
        await message.answer("ВЫБЕРИТЕ ФУНКЦИЮ", reply_markup=func_markup)
        await Test.FUNC1.set()
    elif answer == "ПОЛНАЯ-ПРО ВЕРСИЯ":
        await message.answer("ВЫБЕРИТЕ ФУНКЦИЮ", reply_markup=pro1)
        await Test.FUNC1.set()
    else:
        await message.answer("Введите команду!", reply_markup=b_markup)


@dp.message_handler(state=Test.FUNC1)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "ЗАНЯТИЕ ВМЕСТЕ":
        await message.answer("WEFUNC - Это функция бота с которой вы сможете сделать тренировки вместе.\n"
                             "Пользы функции:\n"
                             "\n"
                             "-Экономит ваше время!\n"
                             "-Подскажет когда делать отдых и как!\n"
                             "-Напоминает о перерывах!\n"
                             "-Удобно, просто!\n"
                             "\n"
                             "Оправляй команду что бы начать.", reply_markup=FUNC)
        await state.finish()
        register_handlers_extra(dp)
    elif answer == "ПЛАН ПИТАНИЯ":
        await message.answer("HEALFUNC - Это функция бота с которой вы сможете узнать сколько вам нужно есть и пить.\n"
                             "Пользы функции:\n"
                             "\n"
                             "-Экономит ваше время!\n"
                             "-Подскажет что есть, сколько есть!\n"
                             "-Какие продукты вам нужно!\n"
                             "-Удобно, просто!\n"
                             "\n"
                             "Оправляй команду что бы начать.", reply_markup=give)
        await state.finish()
        register_handlers_extra1(dp)
    elif answer == "ПРАВИЛЬНАЯ ТЕХНИКА УПРАЖНЕНИЙ":
        await message.answer("TRUEFUNC - Это функция бота с которой вы сможете научиться правильно делать упражнение с техникой.\n"
                             "Пользы функции:\n"
                             "\n"
                             "-Экономит ваше время!\n"
                             "-Подскажет что и как правильно!\n"
                             "-Спасет от травм!\n"
                             "-Удобно, просто!\n"
                             "\n"
                             "Оправляй команду что бы начать.", reply_markup=givetrue)
        await state.finish()
        register_handlers_extraa(dp)
    elif answer == "УВЕЛИЧИТЬ ЖИМ":
       await message.answer("GYMFUNC - Это функция бота с которой вы сможете увеличить свой жим и пожать рекорд!.\n"
                         "Пользы функции:\n"
                         "\n"
                         "-Экономит ваше время!\n"
                         "-Эффективно увеличит ваш жим лежа!\n"
                         "-Подскажет что и как правильно!\n"
                         "-Спасет от травм!\n"
                         "-Удобно, просто!\n"
                         "-Полный план до рекордного жима!\n"
                         "\n"
                         "Оправляй команду что бы начать.", reply_markup=givegym)
       await state.finish()
       register_handlers_extras(dp)
    else:
        await message.answer("Введите команду!")



@dp.message_handler(state=Test.PRO)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "УЗНАТЬ БОЛЬШЕ":
        await message.answer("FULLBODY-PRO - МНОГОФУНКИОНАЛЬНАЯ СБОРКА ВСЕХ ТИПОВ САМОРАЗВИТИЯ И ФУНКЦИЙ.\n"
                             "\n"
                             "ЧТО ВКЛЮЧАЕТ В СЕБЯ:\n"
                             "\n"
                             "-1.Персональные рекомендации - учитывая ваши уникальности!\n"
                             "-2.Прямое обращение к тренеру!\n"
                             "-3.Уникальные функции!\n"
                             "-4.План тренировок!\n"
                             "-5.Рекомендациями по всем критериям внешности-\n"
                             "\n"
                             "                  -Рост\n"
                             "                  -Кожа\n"
                             "                  -Тестостерон\n"
                             "                  -Тело\n"
                             "\n"
                             "-6.Персональные, личные советы!", reply_markup=pro)

        await Test.PRO1.set()


@dp.message_handler(state=Test.PRO1)
async def answer_end(message: types.Message, state: FSMContext):
        answer = message.text.strip()
        if answer == "ЧЕМ СДЕЛАЕТ МЕНЯ ЛУЧШЕ?":
            await message.answer("Сделает вас лучше:\n"
            "\n"
            "-Дисциплиной!\n"
            "-Персональным планом тренировок!\n"
            "-Персональным планом питания!\n"
            "-Личным тренером!\n"
            "-Правильной техникой!\n"
            "-Персональными советами!\n"
            "-Уникальными функциями!\n"
            "\n"
            "ПОЛНАЯ ВЕРСИЯ БУДЕТ ДОСТУПНА ПОЗЖЕ!")
            await message.answer("Отправлй команду (/start) что бы начать с начало!")
        await state.finish()



@dp.message_handler(state=Test.FUNC2)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "ПЛАН ПИТАНИЯ":
        await message.answer("HEALFUNC - Это функция бота с которой вы сможете узнать сколько вам нужно есть и пить.\n"
                             "Пользы функции:\n"
                             "\n"
                             "-Экономит ваше время!\n"
                             "-Подскажет что есть, сколько есть!\n"
                             "-Какие продукты вам нужно!\n"
                             "-Удобно, просто!\n"
                             "\n"
                             "Оправляй команду что бы начать.", reply_markup=give)
        await state.finish()
        register_handlers_extra1(dp)


@dp.message_handler(state=Test.END)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    data = await state.get_data()  # Получение всех ответов
    q1 = data.get('q1')
    q2 = data.get('q2')
    q3 = data.get('q3')
    q4 = data.get('q4')
    q5 = data.get('q5')
    q6 = data.get('q6')
    q7 = data.get('q7')
    q4 = float(q4)
    q5 = float(q5)
    q3 = float(q3)

    q3 = "{:.2f}".format(q3 / 100)
    q3 = float(q3)
    bmi = q5 / (q3 ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
            with open('Untitled (38).png', 'rb') as photo:
                await message.answer_photo(photo)
                await message.answer(f"Ваш (ИМТ) Индекс Массы Тела низкий(МАССА ТЕЛА НИЗКАЯ):{bmi}\n"
                                     f"ДЛЯ НАБОРА МАССЫ:\n"
                                     f"\n"
                                     f"Персональный совет: Снизьте активность(занимайтесь тренировками)\n"
                                     f"\n"
                                     f"Не утомляйтесь, не добивайте себя, следите за питанием ешьте больше.\n"
                                     f"\n")
                await message.answer("Обработка вашего запроса...")
                delay_seconds = 5
                await asyncio.sleep(delay_seconds)
                await message.answer("Программа тренировок готова!")
                await message.answer("https://disk.yandex.ru/d/m1ejkLXAt7gffQ")
                delay_seconds = 4
                await asyncio.sleep(delay_seconds)
                with open('Untitled (46).png', 'rb') as photo:
                    await message.answer_photo(photo)
                delay_seconds = 4
                await asyncio.sleep(delay_seconds)
                await message.answer("Обработка...")
                delay_seconds = 4
                await asyncio.sleep(delay_seconds)
                with open('НИЗ-ПН1.MP4', 'rb') as video:
                    await message.answer_video(video)
                    await message.answer("ПОНЕДЕЛЬНИК ДЕНЬ-1")
                    with open('НИЗ-ВТ.MP4', 'rb') as video:
                        await message.answer_video(video)
                        await message.answer("СРЕДА ДЕНЬ-2")
                        with open('НИЗ-ПТ1.MP4', 'rb') as video:
                            await message.answer_video(video)
                            await message.answer("ПЯТНИЦА ДЕНЬ-3")
                    with open('ЧЕК ЛИСТ01.jpg', 'rb') as photo:
                        await message.answer_photo(photo)
                        await message.answer("Получить дальнейшие инструкции?", reply_markup=instruc)
                        await Test.ENDFUNC.set()



    elif 18.5 <= bmi <= 24.9:
        with open('Untitled (37).png', 'rb') as photo:
            await message.answer_photo(photo)
            await message.answer(f"Ваш (ИМТ) Индекс Массы Тела в норме:{bmi}\n"
                                                                      f"ДЛЯ НАБОРА МАССЫ:\n"
                                 f"\n"

                           f"Персональный совет: Снизьте активность(занимайтесь тренировками)\n"
                           f"и не утомляйтесь, не добивайте себя, следите за питанием ешьте больше.\n"
                           f"\n")
            await message.answer("Обработка вашего запроса...")
            delay_seconds = 5
            await asyncio.sleep(delay_seconds)
            await message.answer("Программа тренировок готова!")
            delay_seconds = 4
            await asyncio.sleep(delay_seconds)
            with open('Untitled (46).png', 'rb') as photo:
                await message.answer_photo(photo)
            delay_seconds = 2
            await asyncio.sleep(delay_seconds)
            await message.answer("Обработка...")
            delay_seconds = 3
            await asyncio.sleep(delay_seconds)
            random_numbers = int(''.join(str(random.randint(1, 9)) for _ in range(10)))
            with open('НОРМ-ПН1.MP4', 'rb') as video:
                await message.answer_video(video)
                await message.answer("ПОНЕДЕЛЬНИК ДЕНЬ-1")
                with open('НОРМ-СР1.MP4', 'rb') as video:
                    await message.answer_video(video)
                    await message.answer("СРЕДА ДЕНЬ-2")
                    with open('НОРМ-ПТ.MP4', 'rb') as video:
                        await message.answer_video(video)
                        await message.answer("ПЯТНИЦА ДЕНЬ-3")
                with open('ЧЕК ЛИСТ01.jpg', 'rb') as photo:
                    await message.answer_photo(photo)
                    await message.answer("Получить дальнейшие инструкции?", reply_markup=instruc)
                    await Test.ENDFUNC.set()

    elif 24.9 <= bmi <= 30:
        with open('Untitled (31).png', 'rb') as photo:
            await message.answer_photo(photo)
            await message.answer(f"Ваш (ИМТ) Индекс Массы Тела в избытке (лишний вес){bmi}\n"
                                                                      f"ДЛЯ НАБОРА МАССЫ И СНИЖЕНИЕ ЖИРОВ:\n"
                                 f"\n"

                                 f"Ваш персональный совет:Двигайтесь больше, не утомляйтесь, пейте больше воды,\n"
                                 f"ограничьте жиры потребление сладкого и жиров")
            await message.answer("Обработка вашего запроса...")
            delay_seconds = 5
            await asyncio.sleep(delay_seconds)
            await message.answer("Программа тренировок готова!")
            delay_seconds = 4
            await asyncio.sleep(delay_seconds)

            with open('Untitled (46).png', 'rb') as photo:
                await message.answer_photo(photo)
            delay_seconds = 2
            await asyncio.sleep(delay_seconds)
            await message.answer("Обработка...")
            delay_seconds = 3
            await asyncio.sleep(delay_seconds)
            random_numbers = int(''.join(str(random.randint(1, 9)) for _ in range(10)))
            with open('ИЗБ-ПН.MP4', 'rb') as video:
                await message.answer_video(video)
                await message.answer("ПОНЕДЕЛЬНИК ДЕНЬ-1")
                with open('ИЗБ-СР.MP4', 'rb') as video:
                    await message.answer_video(video)
                    await message.answer("СРЕДА ДЕНЬ-2")
                    with open('ИЗБ-ПН.MP4', 'rb') as video:
                        await message.answer_video(video)
                        await message.answer("ПЯТНИЦА ДЕНЬ-3")
                with open('ЧЕК ЛИСТ01.jpg', 'rb') as photo:
                    await message.answer_photo(photo)
                    await message.answer("Получить дальнейшие инструкции?", reply_markup=instruc)
                    await Test.ENDFUNC.set()

    elif 30 <= bmi:
        with open('Untitled (41).png', 'rb') as photo:
            await message.answer_photo(photo)
            await message.answer(f"Ваш (ИМТ) Индекс Массы Тела в избытке слишком(лишний вес){bmi}\n"
                                                                      f"ДЛЯ НАБОРА МАССЫ И СНИЖЕНИЕ ЖИРА:\n"
                                 f"\n"

                                 f"Ваш персональный совет: Двигайтесь больше, ходите больше ешьте больше,"
                                 f" не утомляйтесь."
                                 f"Так же занимайтесь под наблюдением тренеров и получите консультацию с врачами.")
            await message.answer("Обработка вашего запроса...")
            delay_seconds = 5
            await asyncio.sleep(delay_seconds)
            await message.answer("Программа тренировок готова!")
            delay_seconds = 4
            await asyncio.sleep(delay_seconds)

            with open('Untitled (46).png', 'rb') as photo:
                await message.answer_photo(photo)
            delay_seconds = 2
            await asyncio.sleep(delay_seconds)
            await message.answer("Обработка...")
            delay_seconds = 3
            await asyncio.sleep(delay_seconds)
            random_numbers = int(''.join(str(random.randint(1, 9)) for _ in range(10)))
            with open('ОЧИЗБ-ПН.MP4', 'rb') as video:
                await message.answer_video(video)
                await message.answer("ПОНЕДЕЛЬНИК ДЕНЬ-1")
                with open('ОЧИЗБ-СР.MP4', 'rb') as video:
                    await message.answer_video(video)
                    await message.answer("СРЕДА ДЕНЬ-2")
                    with open('ОЧИЗБ-ПТ.MP4', 'rb') as video:
                        await message.answer_video(video)
                        await message.answer("ПЯТНИЦА ДЕНЬ-3")
                with open('ЧЕК ЛИСТ.jpg', 'rb') as photo:
                    await message.answer_photo(photo)
                    await message.answer("Получить дальнейшие инструкции?", reply_markup=instruc)
                    await Test.ENDFUNC.set()
    else:
        await message.answer('Не удалось обработать ваши данные.Пожалуйста пройдите заново и постарайтесь корректно '
                             'ввести данные!\n''Что бы пройти заново отправьте команду {/start}')
        await state.finish()


@dp.message_handler(state=Test.ENDFUNC)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == "ПОЛУЧИТЬ ИНСТРУКЦИЮ":
        await message.answer("После полной недели тренировок.\n"
                             "\n"
                             "-Проанализируйте свой прогресс\n"
                             "-Учтите недостатки в программе\n"
                             "-Найдите более подходящий подход к тренировкам\n"
                             "\n"
                             "ЧТО НУЖНО ДЕЛАТЬ ДАЛЬШЕ?\n"
                             "1.Усовершенствуйте план тренировок с помощью самоанализа.\n"
                             "2.Вычитайте и добавляйте упражнение.\n"
                             "\n"
                             "ОЖИДАЙТЕ ОБРАТНОЙ СВЯЗИ ОТ НАС!\n"
                             "\n"
                             "ВНИМАНИЕ! Мы не можем вам дать самые точные советы и планы тренировок так как у нас недостаточно "
                             "информаций о вашей здоровьи и уникальных отличий и по этому просим вас самоанализировать "
                             "ваши действия. С уважением команда - [FULLBODY]")
        await message.answer("Вы в меню выберите команду:", reply_markup=b_markup)
        await Test.MENU.set()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)




