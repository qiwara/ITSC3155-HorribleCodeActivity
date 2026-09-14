def add():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number + second_number)

    again = input("Would you like to perform another addition? ")
    while (again == "yes"):
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))
        print(first_number + second_number)
        again = input("Would you like to perform another addition? ")

    result = first_number + second_number
def subtract():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number - second_number)

    again = input("Would you like to perform another subtraction? ")
    while (again == "yes"):
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))
        print(first_number - second_number)
        again = input("Would you like to perform another subtraction? ")

def multiply():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number * second_number)

    again = input("Would you like to perform another multiplication? ")
    while (again == "yes"):
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))
        print(first_number * second_number)
        again = input("Would you like to perform another multiplication? ")

def divide():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    if second_number == 0:
        print("You cannot divide by zero!")
    else:
        print(first_number / second_number)

    again = input("Would you like to perform another division? ")
    while (again == "yes"):
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))
        if second_number == 0:
            print("You cannot divide by zero!")
            again = input("Would you like to perform another division? ")
        else:
            print(first_number / second_number)
            again = input("Would you like to perform another division? ")

while True:
    print("====================================")
    print("             CALCULATOR 3000")
    print("====================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("====================================")
    choice = input("Please select an operation: ")
    if choice == "1":
     add()
    elif choice == "2":
      subtract()
    elif choice == "3":
      multiply()
    elif choice == "4":
        divide()
    elif choice == "5":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid selection, try again.")