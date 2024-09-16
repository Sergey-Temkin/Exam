from Data.read_save import read_json
from Car.actions import calculate
from Car.menu import menu_selection
from icecream import ic 

# Main menu function
# calculate() - function that calculates all cars in garage and total incomes
# menu_selection() - function that sends "garage" information and "choice" to functions methods    
def menu(garage):
    while True:
        calculate(garage)
        print("-----------------------------------------")
        ic("Garage menu:")
        print("1 - List all cars")
        print("2 - Add car")
        print("3 - Delete car")
        print("4 - Search car")
        print("5 - Save & Exit")
        print("-----------------------------------------")
        choice=input("Select option:")
        print("-----------------------------------------")
        menu_selection(garage,choice)
        if choice == "5":
            print("Saving & Exiting")
            print("-----------------------------------------")
            break

def main():
    garage=read_json()
    return menu(garage)

if __name__ == "__main__":
    main()
