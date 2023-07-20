import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

randomLetters = []
for number in range(0, nr_letters):
    rand = letters[random.randint(0, len(letters) - 1)]
    randomLetters.append(rand)
print(randomLetters)

randomSymbols = []
for number in range(0, nr_symbols):
    rand = symbols[random.randint(0, len(symbols) - 1)]
    randomSymbols.append(rand)
print(randomSymbols)

randomNumbers = []
for number in range(0, nr_numbers):
    rand = numbers[random.randint(0, len(numbers) - 1)]
    randomNumbers.append(rand)
print(randomNumbers)

password = f"{''.join(randomLetters)}{''.join(randomSymbols)}{''.join(randomNumbers)}"
print(f"My password: {password}")


# HARD. RANDOMIZE THE CHARACTERS IN THE PASSWORD
pass_arr = [*password]
random.shuffle(pass_arr)
print(f"My random password: {''.join(pass_arr)}")
