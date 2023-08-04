alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

size = len(alphabet) - 1

def caesar_cypher(text, shift, direction):
    encrypted_word = ""
    for l in text:
        if l not in alphabet: encrypted_word += l
        if l in alphabet:
            index = alphabet.index(l)
            if direction == "encode":
                if index + shift > size:
                    can_cover = size - index
                    encrypted_word += alphabet[shift - can_cover - 1]
                else:
                    encrypted_word += alphabet[index + shift]
            else:
                if index - shift < 0:
                    can_cover = shift - index
                    encrypted_word += (alphabet[-can_cover])
                else:
                    encrypted_word += alphabet[index - shift]

    print(encrypted_word)


def start_program():
    play = True
    while play:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar_cypher(text, shift, direction)
        choice = input("Type 'yes' if you want to run the program again. If not, type 'no'").lower()
        if not choice == "yes": play = False

start_program()
