from keyboards.inline.callback_datas import menu_cd, buy_item
from requests import get, post, delete


def make_callback_data(level, category="0", item_id="0"):
    return menu_cd.new(level=level, category=category, item_id=item_id)


def get_categories():
    return get('http://localhost:5000/api/v2/categories').json()


async def count_items(index):
    inf = await get_items()
    items = inf['items']
    count = 0
    for i in range(len(items)):
        if items[i][1] == index:
            count += 1
    return count


async def get_items():
    return get('http://localhost:5000/api/v2/items').json()


async def get_cat_items(category):
    inf = await get_items()
    items = inf['items']
    right_items = []
    for i in range(len(items)):
        if items[i][1] == category:
            right_items.append(items[i])
    return right_items


async def get_item(id):
    return get(f'http://localhost:5000/api/v2/items/{id}').json()['items']