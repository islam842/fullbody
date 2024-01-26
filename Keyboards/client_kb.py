from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
ans_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НАЧАТЬ!"),
    KeyboardButton("О НАС"),
    KeyboardButton("МЕНЮ"),
    KeyboardButton("ФУНКЦИИ БОТА"),

)


answer_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НАЧАТЬ!"),
    KeyboardButton("ХОЧУ ЗАДАТЬ ВОПРОС"),
    KeyboardButton("МЕНЮ"),



)
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True



).add(
    KeyboardButton("Что такое спортпитание?"),
    KeyboardButton("Что такое тренировки?"),
    KeyboardButton("Как быстро могу набрать массу?"),
    KeyboardButton("Сколько времени стабильно нужно уделять?"),
    KeyboardButton("Чем полезен проект?"),
    KeyboardButton("МЕНЮ")
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("Да"),
    KeyboardButton("Нет"),
)

active_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("Сидячий"),
    KeyboardButton("Умеренный"),
    KeyboardButton("Активный")
)

mot_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("Низкое"),
    KeyboardButton("Среднее"),
    KeyboardButton("Хорошая")
)

one_week = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("Получить недельный чек-лист тренировок."),
)

an_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НАЧАТЬ!"),
)


a_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("О НАС"),
)

b_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НАЧАТЬ!"),
    KeyboardButton("ФУНКЦИИ БОТА"),
    KeyboardButton("ХОЧУ ЗАДАТЬ ВОПРОС")
)

func_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("ЗАНЯТИЕ ВМЕСТЕ"),
    KeyboardButton("ПЛАН ПИТАНИЯ"),
    KeyboardButton("ПРАВИЛЬНАЯ ТЕХНИКА УПРАЖНЕНИЙ")


)

FUNC = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("/wefunc"),
)

healfunc = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НИЗКИЙ"),
    KeyboardButton("НОРМА"),
    KeyboardButton("ИЗБИТОК"),
    KeyboardButton("(СЛШ) ИЗБИТОК")
)


nabor = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("НАБРАТЬ МАССУ")

)


give = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("/healfunc"),

)

kbfinish = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("ЗАВЕРШИТЬ"),
    KeyboardButton("НАЧАТЬ С НАЧАЛА"),

)

gived = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("ПОЛУЧИТЬ")

)


kbfuncthree = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("Как делать жим лёжа?"),
    KeyboardButton("Как делать отжимания?"),
    KeyboardButton("Как делать приседания со штангой?"),
    KeyboardButton("Как делать французкий жим?"),
    KeyboardButton("Как делать подтягивание?"),
    KeyboardButton("Как делать брусья?"),
    KeyboardButton("ЗАВЕРШИТЬ"),


)

givetrue = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("/truefunc"),

)

instruc = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True


).add(
    KeyboardButton("ПОЛУЧИТЬ ИНСТРУКЦИЮ")

)