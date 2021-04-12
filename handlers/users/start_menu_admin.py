from aiogram.dispatcher.filters import Command
from aiogram import types

from data.config import ADMINS
from loader import dp


@dp.message_handler(Command("admin"))
async def show_admin_start(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Приветствуем вас в панели администратора :) \n"
                             "Вот список всех команд: \n"
                             "/start_menu - для входа в меню пользователя \n"
                             "/add_item - для добавления товара \n"
                             "/show_question - для просмотра вопросов по тех.поддержке \n"
                             "/see_all_users - для просмотра всех пользователей бота")
    else:
        await message.answer("У вас нет прав на использование этой команды!")

