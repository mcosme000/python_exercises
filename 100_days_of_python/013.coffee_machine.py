drinks = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, },
        "price": 150
    },
    "latte": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150},
        "price": 250
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100},
        "price": 300
    }
}


coffee_machine = {
    "resources": {"water": 300, "milk": 200, "coffee": 100},
    "money": 0
}

coffee_addict = True
admin_mode = False


def show_resources():
    print("These are the resources:")
    for n in coffee_machine['resources']:
        print(f"{n.capitalize()}: {coffee_machine['resources'][n]}")
    print(f"Money: {coffee_machine['money']}")


def use_resources(ingredients):
    for ingredient in ingredients:
        coffee_machine['resources'][ingredient] -=  ingredients[ingredient]


def proceed_payment(price):
    print(f"This drink costs {price}")
    money = int(input(f"Please insert {price} yen\n> "))
    if money > price:
        print(f"Thank you, here is your change: {money - price}")
    while money < price:
        print(f"Sorry, the amount is not enough. You still need to insert {price - money} yen.")
        money += int(input(f"Please insert {price - money} yen\n> "))
    coffee_machine['money'] += price


def check_resources(ingredients):
    resources = coffee_machine['resources']
    for n in ingredients:
        if ingredients[n] > resources[n]:
            print(f"Sorry, we don't have enough {ingredients[n]}, come back later!")
            return False
    return True


def prepare_drink(order):
    global coffee_addict
    ingredients = drinks[order]['ingredients']
    is_enough = check_resources(ingredients)
    if is_enough:
        use_resources(ingredients)
        proceed_payment(drinks[order]['price'])
        print("Thank you! Your drink is ready, enjoy :)")
        drink_more = input("Do you want another drink? [ YES | NO ]\n").lower()
        if not drink_more == "yes":
            coffee_addict = False


while coffee_addict:
    option = input("What would you like? [ Espresso | Latte | Cappuccino ]\n> ")
    if option == "espresso" or option == "latte" or option == "cappuccino":
        prepare_drink(option)
    elif option == "report":
        show_resources()
    elif option == "off":
        coffee_addict = False
        print("Thank you, bye")
    else:
        print("Select a valid choice")
