from Problems.problems_menu import problem_counter

#list_all_cars() - prints all cars in garage
def list_all_cars(garage: list):
    for car in garage:
        print(f'Car number:{car["car_number"]},Problems{car["problems"]},Total payment:{car["total"]}')

# add_car() - add's new car to garage
# new_car -  add's number of car,all problems,total amount to pay
# # problem_counter() - function that calculates all problems and total amount to pay
def add_car(garage: list):
    car_number=input("Enter new car number:")
    for car in garage:
        if car["car_number"] == car_number:
            print("Car in garage try again!")
            print("-----------------------------------------")
            break
        else:
            new_problem=problem_counter()
            answer=input("Do you wish to enter garage?")
            if answer.lower() == "y":
                new_car={"car_number":car_number , "problems":new_problem[0] , "total":new_problem[1]}
                garage.append(new_car)
                print("Car added!")
                print("-----------------------------------------")
                break
            else:
                print("Goodbye")
                print("-----------------------------------------")
                break

# delete_car() - deletes car from garage
# counter - gives the index car to delete
def delete_car(garage: list):
    counter=0
    for car in garage:
        print(f'Car number:{car["car_number"]},Car index:---{counter}')
        counter+=1
    delete=int(input("Enter car index to delete:"))
    if delete in range(0,counter):
        garage.pop(delete)
        print("Car deleted!")
    else:
        print("Wrong input try again")                  
        print("-----------------------------------------")

# search_car - search's car by number of the car
def search_car(garage: list):
    while True:
        search=input("Enter car number to search:")
        for car in garage:
            if car["car_number"] == search:
                print("Car in garage!")
                print("Press:'0' to exit search mode")
                print("-----------------------------------------")
                break
        else:
            if search == "0":
                break
            print("Car not found,Try again or press:'0' to exit search mode")
            print("-----------------------------------------")

# calculate() - function that calculates all cars in garage and total incomes
def calculate(garage: list):
    counter=0
    for car in garage:
        if "total" in car:
            counter+=car["total"]
    print(f'Total cars in garage:{len(garage)},Total incomes:{counter}')    























