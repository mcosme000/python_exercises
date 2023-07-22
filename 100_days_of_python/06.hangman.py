import random

words_list = ["aardvark", "baboon", "camel", "pancake", "courtain", "counter"]

word = random.choice(words_list)
placeholder = ""

for letter in word:
    placeholder += "_"

placeholder_array = list(placeholder)
print(f"The word you need to guess has {len(placeholder_array)} letters:\n {''.join(placeholder_array)}")

tries = 0

while ("_" in placeholder_array and tries < 8):
    print(f'There are still {placeholder_array.count("_")} letters left')
    letter = input("Guess a letter: \n").lower()
    letter_included = letter in word

    if letter_included:
        print(f'The letter {letter.upper()} is in the word!')
        for index, let in enumerate(word):
            if let == letter:
                placeholder_array[index] = letter.upper()
    else:
        print(f'The letter {letter.upper()} is not included in the word... Keep trying!')

    print(''.join(placeholder_array))
    tries += 1
    if tries > 1: print(f'You have {8 - tries} tries left!')

print("Game finised!")
if ("_" in placeholder_array):
    print("You lost!")
else:
    print(f'Congratulations! You guessed the word! \n{word.upper()}')
