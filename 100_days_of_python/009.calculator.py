import calculator_art

# CALCULATOR

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

is_calculating = True
while is_calculating:
    number1 = int(input("First number \n> "))
    number2 = int(input("Second number \n> "))
    op = input("What operation do you want to do? [ + | - | * | / ]}\n> ")

    while not op in operations:
        print("Wrong command, please chose one of the following: [ + | - | * | / ] ")
        op = input("What operation do you want to do? [ + | - | * | / ]}\n> ")

    print(f"The result is {operations[op](number1, number2)}")
    choice = input("Do you want to use the calculator again? [ YES | NO ]\n ").lower()
    if not choice == "yes": is_calculating = False
