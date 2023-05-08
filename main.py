import logging
from config import bot, dp, TOKEN
import random
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.message import ContentTypes
import requests
from bs4 import BeautifulSoup
from aiogram.utils import executor
import logging
from Keyboards.client_lb import answer_markup, submit_markup, cancel_markup

# Настройка логгирования
logging.basicConfig(level=logging.INFO)


class Test(StatesGroup):
    Q1 = State()  # Состояние для первого вопроса
    Q2 = State()  # Состояние для второго вопроса
    Q3 = State()  # Состояние для третьего вопроса
    Q4 = State()  # Состояние для четвертого вопроса
    Q5 = State()  # Состояние для пятого вопроса
    Q6 = State()  # Состояние для шестого вопроса
    Q7 = State()  # Состояние для седьмого вопроса
    Q8 = State()  # Состояние для восьмого вопроса
    Q9 = State()  # Состояние для девятого вопроса
    Q10 = State()  # Состояние для десятого вопроса
    Q11 = State()  # Состояние для первого вопроса
    Q12 = State()  # Состояние для второго вопроса
    Q13 = State()  # Состояние для третьего вопроса
    Q14 = State()  # Состояние для четвертого вопроса
    Q15 = State()  # Состояние для пятого вопроса
    Q16 = State()  # Состояние для шестого вопроса
    Q17 = State()  # Состояние для седьмого вопроса
    Q18 = State()  # Состояние для восьмого вопроса
    Q19 = State()  # Состояние для девятого вопроса
    Q20 = State()
    END = State()  # Состояние для вывода результатов теста


# Начало теста
@dp.message_handler(commands=['start'])
async def start_test(message: types.Message):
    await message.answer('Салам! Мен сага кесип тандаганга жардам берем. 20 суроого даярсынбы? (ооба)',reply_markup=submit_markup)
    await Test.Q1.set()  # Переход к первому вопросу


# Обработка первого вопроса
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text.strip().lower()
    if answer == 'ооба':
        await message.answer('Эн жакшы! Биринчи суроо:\n'
                             'Дүйнөдө эки гана кесип болсо, экөөнүн ичинен кайсы кесипти тандайт элеңиз?\n'
                             'Кайсы жумушту тандайт элеңиз?\n'
                             '1.Жаныбарларга кам көрүү\n'
                             '2.Машиналарды жана приборлорду тейлөө?', reply_markup=answer_markup)
        await Test.Q2.set()  # Переход ко второму вопросу
    else:
        await message.answer('Сураныч (ооба) басыныз!')


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q1=answer)
        await message.answer('Жакшы! Экинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Оорулуу адамдарга жардам берүү\n'
                             '2.Таблицаларды, диаграммаларды,компьютердик программаларды түзүүнү?', reply_markup=answer_markup)
        await Test.Q3.set()  # Переход к третьему вопросу


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q2=answer) # Сохранение ответа на второй вопрос
        await message.answer('Эн жакшы! Учунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Китеп иллюстрацияларынын, плакаттардын, көркөм открыткалардын сапатына көз салууну\n'
                             '2.Өсүмдүктөрдүн абалына жана өнүгүшүнө мониторинг жүргүзүүнү', reply_markup=answer_markup)
        await Test.Q4.set()# Переход к четвертому вопросу


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q3=answer) # Сохранение ответа на третий вопрос
        await message.answer('Эн жакшы! Тортунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Процесс материалдары(жыгач,кездеме,металл,пластик)\n'
                             '2.Керектөөчүгө товар алып келүүнү(жарнамалоо,сатуу)', reply_markup=answer_markup)
        await Test.Q5.set() # Переход к пятому вопросу


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q4=answer) # Сохранение ответа на четвертый вопрос
        await message.answer('Абдан жакшы! Бешинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Илимий-популярдуу китептерди,макалаларды талкуулоону\n'
                             '2.Көркөм китептерди талкуулоону', reply_markup=answer_markup)
        await Test.Q6.set() # Переход к шестому вопросу


@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q5=answer) # Сохранение ответа на пятый вопрос
        await message.answer('Эн сонун! Алтынчы суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Ар кандай тукумдагы жаш малды багуу\n'
                             '2.Теңтуштарды(же жаш балдарды)кандайдыр бир\
                             аракеттерди жасоого үйрөтүүнү(эмгек,спорт)', reply_markup=answer_markup)
        await Test.Q7.set() # Переход к седьмому вопросу


@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q6=answer) # Сохранение ответа на шестой вопрос
        await message.answer('Эн жакшы! Жетинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Сүрөттөрдү көчүрүү, музыкалык аспаптарды күүлөөнү\n'
                             '2.Ар турду жүктү көтөрүүчү унааны(кран, трактор, тепловоз)айдоону',reply_markup=answer_markup)
        await Test.Q8.set()  # Переход к девятому вопросу


@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q7=answer) # Сохранение ответа на седьмой вопрос
        await message.answer('Жакшы! Сегизинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Адамдар менен баарлашуу,аларга керектүү маалыматты түшүндүрүү(маалымат столунда,экскурсияла)\n'
                             '2.Көргөзмөлөрдү,витриналарды көркөм жасалгалоого, спектаклдерди, концерттерди даярдоого катышуу', reply_markup=answer_markup)
        await Test.Q9.set() # Переход к девятому вопросу


@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q8=answer) # Сохранение ответа на восьмой вопрос
        await message.answer('Абдан жакшы! Тогузунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Ремонт буюмдары(кийим-кече, жабдуулар),турак жай\n'
                             '2.Тексттерден,таблицалардан,фигуралардан каталарды издөө жана оңдоо',reply_markup=answer_markup)
        await Test.Q10.set() # Переход к десятому вопросу


@dp.message_handler(state=Test.Q10)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q9=answer)  # Сохранение ответа на первый вопрос
        await message.answer('Жакшы! Онунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Жаныбарларлы дарылоону\n'
                             '2.Эсептөөлөрдү жүргүзүүнү',reply_markup=answer_markup)
        await Test.Q11.set()  # Переход к третьему вопросу


@dp.message_handler(state=Test.Q11)
async def answer_q11(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q10=answer) # Сохранение ответа на второй вопрос
        await message.answer('Эн жакшы! Он биринчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                             '1.Өсүмдүктөрдүн жаңы сортторун өстүрүүнү\n'
                             '2.Өнөр жай продукциясынын жаңы түрлөрүн долбоорлоо(автоунаа,кийим-кече,үй,тамак-аш)', reply_markup=answer_markup)
        await Test.Q12.set()# Переход к четвертому вопросу


@dp.message_handler(state=Test.Q12)
async def answer_q12(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q11=answer) # Сохранение ответа на третий вопрос
        await message.answer('Жакшы! Он экинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Адамдарын ортосундагы талаш-тартыштарды,чыр-чатакты чечүү, ишендирүү, түшүндүрүү,дем берүү,жасалоону\n'
                         '2.Чиймелерди,схемаларды, таблицаларды түшүнүү(түшүнүү,тактоо,иретке келтирүү)', reply_markup=answer_markup)
        await Test.Q13.set() # Переход к пятому вопросу


@dp.message_handler(state=Test.Q13)
async def answer_q13(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q12=answer) # Сохранение ответа на четвертый вопрос
        await message.answer('Эн жакшы! Он учунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Көркөм чыгармачылык кружокторунун иштерине байкоо жүргүзүүнү\n'
                         '2.Микробдордун жашоосуна байкоо жүргүзүү, изилдөөнү', reply_markup=answer_markup)
        await Test.Q14.set() # Переход к шестому вопросу


@dp.message_handler(state=Test.Q14)
async def answer_q14(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q13=answer) # Сохранение ответа на пятый вопрос
        await message.answer('Эн соонун! Он тортунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Медициналык жабдууларды жана приборлорду тейлөө жана оңдоону\n'
                         '2.Жараат алган,көгөргөн,күйгөн жана башкалар болгон учурда адамдарга медициналык жардам көрсөтүүнү', reply_markup=answer_markup)
        await Test.Q15.set() # Переход к седьмому вопросу


@dp.message_handler(state=Test.Q15)
async def answer_q15(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q14=answer) # Сохранение ответа на шестой вопрос
        await message.answer('Жакшы! Он бешиинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Байкалган кубулуштардын,окуялардын, өлчөнгөн объектилердин так сурөттөмөлөрүн(отчетторун) түзүүнү\n'
                         '2.Көрүлгөн же чагылдырылган окуяларды көркөм сүрөттөө', reply_markup=answer_markup)
        await Test.Q16.set()  # Переход к девятому вопросу


@dp.message_handler(state=Test.Q16)
async def answer_q16(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q15=answer) # Сохранение ответа на седьмой вопрос
        await message.answer('Эн жакшы! Он алтынчы суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Ооруканада лабораториялык изилдөөлөрдү жүргүзүүнү\n'
                         '2.Оорулууларды кабыл алуу,кароо,алар менен сүйлөшүү,дарылоону жазуу', reply_markup=answer_markup)
        await Test.Q17.set() # Переход к девятому вопросу


@dp.message_handler(state=Test.Q17)
async def answer_q17(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q16=answer) # Сохранение ответа на восьмой вопрос
        await message.answer('Абдан жакшы! Он жетиинчи суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Бөлмөлөрдүн дубалдарын, буюмдардын бетин сырдоону\n'
                         '2.Имаратты монтаждоону же приборлорду монтаждоону жүргүзүү', reply_markup=answer_markup)
        await Test.Q18.set() # Переход к десятому вопросу


@dp.message_handler(state=Test.Q18)
async def answer_q18(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q17=answer) # Сохранение ответа на шестой вопрос
        await message.answer('Жакшы! Он сегизинчи суроо:\n Кайсы жумушту тандайт элеңиз?\n'
                         '1.Курбуларынын же жаш курбуларынын театрларша,музейлерге, экскурсияларга, жөө саякаттарга жана башка маданий саякаттарын уюштурууну\n'
                         '2.Сахнада ойноо,концерттерге катышууну', reply_markup=answer_markup)
        await Test.Q19.set()  # Переход к девятому вопросу


@dp.message_handler(state=Test.Q19)
async def answer_q19(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q18=answer) # Сохранение ответа на седьмой вопрос
        await message.answer('Эн жакшы! Он тогузунчу суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Чиймелеп боюнча буюмдун тетиктерин(автоунаа, кийим-кече)чыгаруу, имараттарды \n'
                         '2.Сүрөт тартуу,карталарды көчүрүү', reply_markup=answer_markup)
        await Test.Q20.set() # Переход к девятому вопросу


@dp.message_handler(state=Test.Q20)
async def answer_q20(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q19=answer) # Сохранение ответа на восьмой вопрос
        await message.answer('Адбан жакшы! Жыйырманчы суроо:\nКайсы жумушту тандайт элеңиз?\n'
                         '1.Өсүмдүктөрдүн илдеттерине,токой зыянкечтерине,бакчага каршы күрөшүүнү\n'
                         '2.Клавиатура, машиналарды иштөө (машинка,телетайп ж.б)', reply_markup=answer_markup)
        await Test.END.set() # Переход к десятому вопросу


@dp.message_handler(state=Test.END)
async def answer_end(message: types.Message, state: FSMContext):
    answer = message.text.strip()
    if answer == 'тестти токтотуу':
        await message.answer("Тест токтоду. Кайра отууго (/start) командасын жибериниз")
        await state.finish()
    else:
        await state.update_data(q20=answer)
    data = await state.get_data()  # Получение всех ответов
    q1 = data.get('q1')
    q2 = data.get('q2')
    q3 = data.get('q3')
    q4 = data.get('q4')
    q5 = data.get('q5')
    q6 = data.get('q6')
    q7 = data.get('q7')
    q8 = data.get('q8')
    q9 = data.get('q9')
    q10 = data.get('q10')
    q11 = data.get('q11')
    q12 = data.get('q12')
    q13 = data.get('q13')
    q14 = data.get('q14')
    q15 = data.get('q15')
    q16 = data.get('q16')
    q17 = data.get('q17')
    q18 = data.get('q18')
    q19 = data.get('q19')
    q20 = data.get('q20')
    if q1 == '2' and q2 == '2' and q3 == '1' and q4 == '1' and q5 == '1' and q6 == '2' and q7 == '2' and q8 == '2'\
            and q9 == '1' and q10 == '2' and q11 == '2' and q12 == '2' and q13 == '1' and q14 == '1' and q15 == '1'\
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-Техника'
    elif q1 == '2' and q2 == '2' and q3 == '1' and q4 == '1' and q5 == '1' and q6 == '2' and q7 == '1' and q8 == '2' \
            and q9 == '1' and q10 == '2' and q11 == '2' and q12 == '2' and q13 == '1' and q14 == '1' and q15 == '1' \
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-Техника'
    elif q1 == '2' and q2 == '2' and q3 == '1' and q4 == '1' and q5 == '1' and q6 == '1' and q7 == '1' and q8 == '2' \
            and q9 == '1' and q10 == '2' and q11 == '2' and q12 == '2' and q13 == '1' and q14 == '1' and q15 == '1' \
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-Техника'
    elif q1 == '1' and q2 == '1' and q3 == '2' and q4 == '1' and q5 == '1' and q6 == '1' and q7 == '1' and q8 == '2'\
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '2' and q13 == '2' and q14 == '2' and q15 == '1'\
            and q16 == '1' and q17 == '1' and q18 == '2' and q19 == '2' and q20 == '1':
        result = 'Адам-Жаратылыш'
    elif q1 == '1' and q2 == '1' and q3 == '1' and q4 == '1' and q5 == '1' and q6 == '1' and q7 == '1' and q8 == '2'\
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '2' and q13 == '2' and q14 == '2' and q15 == '1'\
            and q16 == '1' and q17 == '1' and q18 == '2' and q19 == '2' and q20 == '1':
        result = 'Адам-Жаратылыш'
    elif q1 == '2' and q2 == '2' and q3 == '1' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '2'\
            and q9 == '2' and q10 == '2' and q11 == '2' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2'\
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-корком образ'
    elif q1 == '1' and q2 == '2' and q3 == '1' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '2'\
            and q9 == '2' and q10 == '2' and q11 == '2' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2'\
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-корком образ'
    elif q1 == '2' and q2 == '2' and q3 == '1' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '1'\
            and q9 == '2' and q10 == '2' and q11 == '2' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2'\
            and q16 == '2' and q17 == '2' and q18 == '1' and q19 == '1' and q20 == '2':
        result = 'Адам-корком образ'
    elif q1 == '2' and q2 == '1' and q3 == '1' and q4 == '2' and q5 == '1' and q6 == '2' and q7 == '2' and q8 == '2'\
            and q9 == '1' and q10 == '2' and q11 == '2' and q12 == '2' and q13 == '1' and q14 == '1' and q15 == '1'\
            and q16 == '2' and q17 == '2' and q18 == '2' and q19 == '2' and q20 == '2':
        result = 'Адам-адам'
    elif q1 == '2' and q2 == '1' and q3 == '1' and q4 == '2' and q5 == '1' and q6 == '2' and q7 == '2' and q8 == '1'\
            and q9 == '1' and q10 == '2' and q11 == '2' and q12 == '2' and q13 == '1' and q14 == '1' and q15 == '1'\
            and q16 == '2' and q17 == '2' and q18 == '2' and q19 == '2' and q20 == '2':
        result = 'Адам-адам'
    elif q1 == '1' and q2 == '1' and q3 == '2' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '2'\
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2'\
            and q16 == '2' and q17 == '1' and q18 == '1' and q19 == '2' and q20 == '1':
        result = 'Адам-системалык белги'
    elif q1 == '1' and q2 == '1' and q3 == '2' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '2' and q8 == '2' \
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2' \
            and q16 == '2' and q17 == '1' and q18 == '1' and q19 == '2' and q20 == '1':
        result = 'Адам-системалык белги'
    elif q1 == '2' and q2 == '2' and q3 == '2' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '2' \
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2' \
            and q16 == '2' and q17 == '1' and q18 == '1' and q19 == '2' and q20 == '1':
        result = 'Адам-системалык белги'
    elif q1 == '1' and q2 == '2' and q3 == '2' and q4 == '2' and q5 == '2' and q6 == '2' and q7 == '1' and q8 == '2'\
            and q9 == '1' and q10 == '1' and q11 == '1' and q12 == '1' and q13 == '1' and q14 == '2' and q15 == '2'\
            and q16 == '2' and q17 == '1' and q18 == '1' and q19 == '2' and q20 == '1':

        result = 'Адам-системалык белги'
    else:
        result = 'Жыйынтыгыныз так чыкпай калды.Сураныч тестти кайрадан отунуз!\n' \
                 'Кайрадан отууго (/start) командасын жибериниз.'
        await state.finish()

    await message.answer(f'Жоопторунузга рахмат! Сиздин жыйынтык:\n{result}')



#     # получаем данные из состояния
#     data = await state.get_data()
#     # создаем словарь с ответами
#     answers = {
#         "Ответ на вопрос 1": data.get("answer_1"),
#         "Ответ на вопрос 2": data.get("answer_2"),
#         "Ответ на вопрос 3": data.get("answer_3"),
#         "Ответ на вопрос 4": data.get("answer_4"),
#         "Ответ на вопрос 5": data.get("answer_5"),
#         "Ответ на вопрос 6": data.get("answer_6"),
#         "Ответ на вопрос 7": data.get("answer_7"),
#         "Ответ на вопрос 8": data.get("answer_8"),
#         "Ответ на вопрос 9": data.get("answer_9"),
#         "Ответ на вопрос 10": data.get("answer_10")
#     }

#     correct_answers = ['Python', '2003', 'Elon Musk', 'SQL', '1990', 'Кит', 'Bill Gates', 'Swift', 'Объектно-ориентированное программирование', 'Python']
#     # проверяем ответы и делаем выводы
#     if answers["Ответ на вопрос 1"] == correct_answers[0] and answers["Ответ на вопрос 2"] == correct_answers[1] and answers["Ответ на вопрос 3"] == correct_answers[2]:
#         await message.answer("Вы ответили правильно на первые три вопроса!")
#     elif answers["Ответ на вопрос 4"] == correct_answers[3] and answers["Ответ на вопрос 5"] == correct_answers[4] and answers["Ответ на вопрос 6"] == correct_answers[5]:
#         await message.answer("Вы ответили правильно на вопросы 4, 5 и 6!")
#     elif answers["Ответ на вопрос 7"] == correct_answers[6] and answers["Ответ на вопрос 8"] == correct_answers[7] and answers["Ответ на вопрос 9"] == correct_answers[8]:
#         await message.answer("Вы ответили правильно на вопросы 7, 8 и 9!")
#     elif answers["Ответ на вопрос 10"] == correct_answers[9]:
#         await message.answer("Поздравляем, вы ответили правильно на все вопросы!")
#     else:
#         await message.answer("К сожалению, вы не ответили правильно на все вопросы. Попробуйте еще раз!")
#     # сбрасываем состояние
#     await state.finish()

# @dp.message_handler(state=Questions.question_10)
# async def process_answer_10(message: types.Message, state: FSMContext):
#     await state.update_data(answer_10=message.text)
#     data = await state.get_data()
#     correct_answers1 = ["Python", "2003", "Elon Musk", "SQL", "1990", "Кит", "Bill Gates", "Swift", "Функциональное программирование"]
#     answers = {
#             "Ответ на вопрос 1": data.get("answer_1"),
#             "Ответ на вопрос 2": data.get("answer_2"),
#             "Ответ на вопрос 3": data.get("answer_3"),
#             "Ответ на вопрос 4": data.get("answer_4"),
#             "Ответ на вопрос 5": data.get("answer_5"),
#             "Ответ на вопрос 6": data.get("answer_6"),
#             "Ответ на вопрос 7": data.get("answer_7"),
#             "Ответ на вопрос 8": data.get("answer_8"),
#             "Ответ на вопрос 9": data.get("answer_9"),
#             "Ответ на вопрос 10": data.get("answer_10")
#         }
#     if data[answer_1] == "Python":
#         await message.answer("Вы ответили правильно на первые три вопроса!")
#     else:
#         await message.answer("Успешно")
        # elif answers["Ответ на вопрос 4"] == correct_answers[3] and answers["Ответ на вопрос 5"] == correct_answers[
        #     4] and answers["Ответ на вопрос 6"] == correct_answers[5]:
        #     await message.answer("Вы ответили правильно на вопросы 4, 5 и 6!")
        # elif answers["Ответ на вопрос 7"] == correct_answers[6] and answers["Ответ на вопрос 8"] == correct_answers[
        #     7] and answers["Ответ на вопрос 9"] == correct_answers[8]:
        #     await message.answer("Вы ответили правильно на вопросы 7, 8 и 9!")
        # elif answers["Ответ на вопрос 10"] == correct_answers[9]:
        #     await message.answer("Поздравляем, вы ответили правильно на все вопросы!")
        # else:
        #     await message.answer("К сожалению, вы не ответили правильно на все вопросы. Попробуйте еще раз!")
        # # сбрасываем состояние
        # await state.finish()
 # and answers["Ответ на вопрос 2"] == correct_answers1[1] and \
            # answers["Ответ на вопрос 3"] == correct_answers1[2] and answers["Ответ на вопрос 4"] == correct_answers1[3]\
            # and answers["Ответ на вопрос 5"] == correct_answers1[4] and answers["Ответ на вопрос 6"] == \
            # correct_answers1[5] and answers["Ответ на вопрос 7"] == correct_answers1[6] and \
            # answers["Ответ на вопрос 8"] == correct_answers1[7] and answers["Ответ на вопрос 9"] == correct_answers1[8]:

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

