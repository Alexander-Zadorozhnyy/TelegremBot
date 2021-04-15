from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from db import db_session
from db.users import User
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    name_user = message.from_user.first_name
    db_sess = db_session.create_session()
    if db_sess.query(User.id).filter(User.id == user_id).all():
        user = User(id_user=user_id, name_user=name_user)
        db_sess.add(user)
        db_sess.commit()
    await message.answer(f"Привет, {message.from_user.full_name}!"
                         f"Жми /start_menu")
