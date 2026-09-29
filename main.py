from menu import add_menu, search_menu, view_menus, edit_menu, delete_menu
from storage import load_menus, save_menus


load_menus()


while True:

    print("\n========== MESS MENU MANAGER ==========")
    print("1. Student")
    print("2. Mess Incharge")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        day = input("Enter day: ").capitalize()

        menu = search_menu(day)

        if menu is not None:

            print("\n========== " + day.upper() + " MENU ==========")

            print("\nBreakfast:")
            print(menu["Breakfast"])

            print("\nLunch:")
            print(menu["Lunch"])

            print("\nSnacks:")
            print(menu["Snacks"])

            print("\nDinner:")
            print(menu["Dinner"])

        else:
            print("Menu not available for this day.")

    elif choice == "2":

        while True:

            print("\n========== MESS INCHARGE ==========")
            print("1. Add Menu")
            print("2. Edit Menu")
            print("3. Delete Menu")
            print("4. View All Menus")
            print("5. Back")

            incharge_choice = input("Enter your choice: ")

            if incharge_choice == "1":

                day = input("Enter day: ").capitalize()

                breakfast = input("Enter breakfast: ")
                lunch = input("Enter lunch: ")
                snacks = input("Enter snacks: ")
                dinner = input("Enter dinner: ")

                add_menu(day, breakfast, lunch, snacks, dinner)
                save_menus()

                print("Menu added successfully!")

            elif incharge_choice == "2":

                day = input("Enter day to edit: ").capitalize()

                if search_menu(day) is not None:

                    breakfast = input("Enter new breakfast: ")
                    lunch = input("Enter new lunch: ")
                    snacks = input("Enter new snacks: ")
                    dinner = input("Enter new dinner: ")

                    edit_menu(day, breakfast, lunch, snacks, dinner)
                    save_menus()

                    print("Menu updated successfully!")

                else:
                    print("Menu not found.")

            elif incharge_choice == "3":

                day = input("Enter day to delete: ").capitalize()

                if delete_menu(day):
                    save_menus()
                    print("Menu deleted successfully.")
                else:
                    print("Menu not found.")

            elif incharge_choice == "4":

                data = view_menus()

                if len(data) == 0:
                    print("No menus available.")

                else:

                    for day in data:

                        print("\n========== " + day.upper() + " ==========")

                        print("Breakfast:", data[day]["Breakfast"])
                        print("Lunch:", data[day]["Lunch"])
                        print("Snacks:", data[day]["Snacks"])
                        print("Dinner:", data[day]["Dinner"])

            elif incharge_choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":

        print("Thank you for using Mess Menu Manager!")
        break


    else:
        print("Invalid choice. Please try again.")
