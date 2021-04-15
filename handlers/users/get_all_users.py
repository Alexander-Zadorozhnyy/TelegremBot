from aiogram import types
from aiogram.dispatcher.filters import Command
from asyncio import sleep

from data.config import ADMINS
from db import db_session
from db.users import User
from loader import dp, bot
from states.commands import get_users


@dp.message_handler(Command('show_all_users'))
async def show_users(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Список пользователей зарегистрированных на сайте: \n")
        users = await get_users()
        for i in range(len(users)):
            await message.answer(f'имя - {users[i]["name_user"]} \nid - {users[i]["id_user"]} \n'
                                 f'email - {users[i]["email_user"]} \nдата создания - {users[i]["created_date"]}')
    else:
        await message.answer("У вас нет прав на использование этой команды!")


@dp.message_handler(Command('see_all_users'))
async def show_users(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Список пользователей, которые используют телеграмм бота: \n")
        session = db_session.create_session()
        news = session.query(User.id_user, User.name_user).all()
        for i in news:
            await message.answer(f'id - {i[0]} \nname - {i[1]}')
    else:
        await message.answer("У вас нет прав на использование этой команды!")
