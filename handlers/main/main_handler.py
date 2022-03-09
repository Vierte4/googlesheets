import datetime

from aiogram.dispatcher import FSMContext
from keyboards.default import organizators_main_keyboard
from keyboards.inline import category_keyboard, category_cb, position_kb, position_cb, choose_kb, choose_cb
from loader import dp
from data.config import USERS
from aiogram import types
from aiogram.types import CallbackQuery
from states import GetPosition
from utils.bot_utils import *
from utils import update_table

@dp.message_handler(state='*', text='Отмена', user_id=USERS)
async def show_current_folder(message: types.Message, state: FSMContext):
    await delete_last_message(message)
    await message.answer('Действие отменено')
    await state.finish()


@dp.message_handler(commands='Start', user_id=USERS)
async def send_main_kb(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=organizators_main_keyboard)


@dp.message_handler(text='Оформить продажу', user_id=USERS)
async def choose_category(message: types.Message):
    await message.answer(text='Нажмите, чтобы продолжить:', reply_markup=position_kb)


@dp.callback_query_handler(position_cb.filter(), user_id=USERS)
async def choose_category(call: types.CallbackQuery):
    await delete_last_message_call(call)
    await call.message.answer(text='Выберите категорию:', reply_markup=category_keyboard())


@dp.callback_query_handler(category_cb.filter(), user_id=USERS)
async def show_current_folder(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await delete_last_message_call(call)
    await call.message.answer(text='Введите количество')
    await GetPosition.quantity.set()
    await state.update_data(category=callback_data.get('category_name'))


@dp.message_handler(state=GetPosition.quantity, user_id=USERS)
async def show_current_folder(message: types.Message, state: FSMContext):
    await delete_last_message(message)
    try:
        await state.update_data(quantity=int(message.text))
        await message.answer('Введите сумму')
        await GetPosition.summ.set()
    except:
        await message.answer('Отправьте в сообщении число или нажмите кнопку "Отмена"')
        return


@dp.message_handler(state=GetPosition.summ, user_id=USERS)
async def show_current_folder(message: types.Message, state: FSMContext):
    await delete_last_message(message)
    try:
        await state.update_data(summ=int(message.text))

        data = await state.get_data()
        category = data.get('category')
        summ = data.get('summ')
        quantity = data.get('quantity')

        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M").split(' ') # Получаем текущие дату и время

        update_table([now[0], now[1], category,quantity , summ])

        await message.answer('Готово!\n'
                             'Вы добавили:\n'
                             f'Категория: {category}\n'
                             f'Количество: {quantity}\n'
                             f'Сумма: {summ}')

        await state.finish()
        await message.answer(text='Добавить ещё одну позицию?', reply_markup=choose_kb)
    except:
        await message.answer('Отправьте в сообщении число или нажмите кнопку "Отмена"')
        return

@dp.callback_query_handler(choose_cb.filter(), user_id=USERS)
async def choose_category(call: types.CallbackQuery, callback_data: dict):
    await delete_last_message_call(call)
    if callback_data.get('variant') == 'Y':
        await call.message.answer(text='Выберите категорию:', reply_markup=category_keyboard())
    else:
        await delete_curent_message_call(call)
