from aiogram.dispatcher.filters.state import StatesGroup, State

class GetPosition(StatesGroup):
    category = State()
    summ = State()
    quantity = State()
