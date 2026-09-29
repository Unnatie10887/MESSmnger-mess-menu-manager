from menu import menus
def save_menus():
    file = open("menu.txt", "w")
    for day in menus:
        menu = menus[day]

        file.write(day + "~")
        file.write(menu["Breakfast"] + "~")
        file.write(menu["Lunch"] + "~")
        file.write(menu["Snacks"] + "~")
        file.write(menu["Dinner"] + "\n")
    file.close()

def load_menus():
    file = open("menu.txt", "r")
    for line in file:
        data = line.strip().split("~")

        if len(data) == 5:
            day = data[0]

            menus[day] = {
                "Breakfast": data[1],
                "Lunch": data[2],
                "Snacks": data[3],
                "Dinner": data[4]
            }
    file.close()
