def add():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number + second_number)

    result = first_number + second_number
def subtract():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number - second_number)

def multiply():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    print(first_number * second_number)

def divide():
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    if second_number == 0:
        print("You cannot divide by zero!")
    else:
        print(first_number / second_number)

print("====================================")
print("             CALCULATOR 3000")
print("====================================")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
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
else:
    print("Invalid selection.")

print("Thank you for using the calculator!")
