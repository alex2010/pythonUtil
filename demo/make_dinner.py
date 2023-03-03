menu = [
    {
        'name': 'GBJD',
        'meat': 2,
        'isRaw': False
    },
    {
        'name': 'YXRS',
        'meat': 1
    }
]

material = {
    'meat': 30,
    'veg': 20
}


def prepare(materials):
    return True


def make_dinner(menu, materials):
    dish_list = []
    prepare(materials)

    if len(menu) > 0:
        # steps
        for it in menu:
            if make_dish(it, materials):
                dish_list.append({'name': it['name'], 'status': 'ready'})
            else:
                dish_list.append({'name': it['name'], 'status': 'err'})
    else:
        print('No menu, plz input menu')
    return dish_list


def make_dish(item, ma):
    if is_enough(item, ma):
        return True
    else:
        return False


def is_enough(dish, materials):
    return True


dishes = make_dinner(menu, material)
print(dishes)
