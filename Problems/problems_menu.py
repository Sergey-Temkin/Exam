from Problems.problems import problems_list

# problem_display() - function that displays all cars in garage by car number and total price to pay
def problem_display():
    for problem in problems_list:
        print(f"Problem:{problem["problem"]},Price:{problem["price"]}")


# problem_counter() - function that calculates all problems and total amount to pay
# counter - counts all problem prices
# problem_arr - saves all problems chosen
def problem_counter():
    counter=0
    problem_arr=[]
    while True:
        problem_display()
        print("--------")
        print("To add Engine problem press - 1")
        print("To add Breaks problem press - 2")
        print("To add 5000km treatment press - 3")
        print("To add 10000km treatment press - 4")
        print("To add Filters&Oil problem press - 5")
        print("To add Gear problem press - 6")
        print("To save & exit press - 7")
        choice=input("Input select :")
        if choice == "1" :
            counter+=2000
            problem_arr.append(problems_list[0])
        elif choice == "2" :
            counter+=1000
            problem_arr.append(problems_list[1])
        elif choice == "3" :
            counter+=500
            problem_arr.append(problems_list[2])
        elif choice == "4" :
            counter+=1000
            problem_arr.append(problems_list[3])
        elif choice == "5" :
            counter+=250
            problem_arr.append(problems_list[4])
        elif choice == "6" :
            counter+=1000
            problem_arr.append(problems_list[5])
        elif choice == "7" :
            print(f"All problems:\n {problem_arr}\nTotal price:{counter}")
            return problem_arr , counter
        else:
            print("Wrong input try again!")
            print("----------------------")
