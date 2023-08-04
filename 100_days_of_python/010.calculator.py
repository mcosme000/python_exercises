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

def calculator():
    print(calculator_art.logo)
    number1 = float(input("Pick a number: \n> "))
    is_calculating = True

    while is_calculating:
        op = input("Pick an operation [ + | - | * | / ]}\n> ")
        number2 = float(input("What is the next number? \n> "))

        while not op in operations:
            print("Wrong command, please chose one of the following: [ + | - | * | / ] ")
            op = input("What operation do you want to do? [ + | - | * | / ]}\n> ")

        result = operations[op](number1, number2)
        print(f"{number1} {op} {number2} = {result}")
        print("What do you want to do next?")
        print(f"[ 1 ] Continue calculating with {result}")
        print("[ 2 ] Calculate with two other numbers")
        print("[ 3 ] Exit calculator")
        choice = int(input("> "))
        match choice:
            case 1:
                number1 = result
            case 2:
                is_calculating = False
                calculator()
            case 3: is_calculating = False

calculator()
