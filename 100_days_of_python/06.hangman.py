import random
import words_list
import hangman_art

word = random.choice(words_list.word_list)

placeholder = []

for _ in word: placeholder.append("_")

print(f"The hidden word has {len(placeholder)} letters:\n{' '.join(placeholder)}")

tries = 0

while ("_" in placeholder and tries <= 6):
    letter = input("Guess a letter: ").lower()
    for index, let in enumerate(word):
        if let == letter:
            placeholder[index] = letter.upper()

    print(' '.join(placeholder))
    tries += 1
    if tries >= 1:
        print(f'{hangman_art.stages[-tries]}\n')

print("Game finised!")

if ("_" in placeholder):
    print(f"You lost! The word was {word}")
else:
    print(f'Congratulations! You guessed the word! \n{word.upper()}')


"""
Other way of doing this is to create end_of_game = False
if "_" not in placeholder: end_of_game = True
"""
