from typing import Union
from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.inline import menu_cd
from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, item_keyboard
from states.commands import get_item, get_image
from loader import dp


@dp.message_handler(Command("show_question"))
async def show_question():
