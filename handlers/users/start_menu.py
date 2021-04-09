from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from aiogram import types

from keyboards.inline import menu_cd
from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, item_keyboard
from keyboards.inline.commands import get_item
from loader import dp


@dp.message_handler(Command("start_menu"))
async def show_start_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        await message.answer("В нашем магазине предствалены товары нижеперечисленных категорий:", reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_items(callback: types.CallbackQuery, category, **kwargs):
    markup = await items_keyboard(category=category)
    await callback.message.edit_text("По вашей категории нашлось:", reply_markup=markup)


async def show_item(callback: types.CallbackQuery, category, item_id):
    markup = item_keyboard(category, item_id)
    item = await get_item(item_id)
    text = f"Вы можете преобрести: {item['name']} \n"
    txt = item['characteristics'].split('%')
    all_str = str('Характеристики устройства---->\n')
    for el in range(0, len(txt), 2):
        all_str = '\n'.join([all_str, ':   '.join([txt[el], txt[el + 1]])])
    text = ''.join([text, all_str])
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    item_id = callback_data.get('item_id')

    levels = {
        "0": list_categories,
        "1": list_items,
        "2": show_item
    }

    current_Level_function = levels[current_level]

    await current_Level_function(call,
                                 category=category,
                                 item_id=item_id
    )
