from Data.read_save import save_json
from Car.actions import list_all_cars,add_car,delete_car,search_car

# menu_selection() - function that sends "garage" information and "choice" to functions methods
def menu_selection(garage,choice):
    if choice == "1":
        return list_all_cars(garage)
    elif choice == "2":
        return add_car(garage)
    elif choice == "3":
        return delete_car(garage)
    elif choice == "4":
        return search_car(garage)
    elif choice == "5":
        return save_json(garage)
    else:
        print("Wrong input try again!")
        print("----------------------")
    