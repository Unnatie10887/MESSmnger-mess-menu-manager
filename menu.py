menus = {}


def add_menu(day, breakfast, lunch, snacks, dinner):
    menus[day] = {
        "Breakfast": breakfast,
        "Lunch": lunch,
        "Snacks": snacks,
        "Dinner": dinner
    }


def search_menu(day):
    if day in menus:
        return menus[day]
    else:
        return None


def view_menus():
    return menus


def edit_menu(day, breakfast, lunch, snacks, dinner):
    if day in menus:
        menus[day] = {
            "Breakfast": breakfast,
            "Lunch": lunch,
            "Snacks": snacks,
            "Dinner": dinner
        }
        return True
    else:
        return False


def delete_menu(day):
    if day in menus:
        del menus[day]
        return True
    else:
        return False
