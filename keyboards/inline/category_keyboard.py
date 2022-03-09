from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.config import category_path

category_cb = CallbackData("category", "category_name")
position_cb = CallbackData("position")
choose_cb = CallbackData("choose", 'variant')

position_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Добавить позицию', callback_data=position_cb.new()))


choose_kb = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Да', callback_data=choose_cb.new(variant='Y')),
    InlineKeyboardButton(text='Нет', callback_data=choose_cb.new(variant='N')))

def category_keyboard():
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    file = open(category_path, encoding='utf-8')
    list = file.read().split('\n')
    file.close()

    kboard = InlineKeyboardMarkup()

    for note in list:
        kboard.add(InlineKeyboardButton(text=note, callback_data=category_cb.new(category_name=note)))
    return kboard