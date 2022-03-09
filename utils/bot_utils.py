import aiogram.types
from loader import bot


async def delete_last_message(message: aiogram.types.Message):
    # Скрывает последнюю отправленную клавиатуру
    try:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 1)
    except:
        pass


async def delete_last_message_call(call: aiogram.types.CallbackQuery):
    # Скрывает последнюю отправленную клавиатуру
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
    except:
        pass

async def delete_curent_message_call(call: aiogram.types.CallbackQuery):
    # Скрывает последнюю отправленную клавиатуру
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    except:
        pass