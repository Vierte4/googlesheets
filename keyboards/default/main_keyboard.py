from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

organizators_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оформить продажу')
        ],
        [
            KeyboardButton(text='Отмена')
        ],

    ],
    resize_keyboard=True
)
