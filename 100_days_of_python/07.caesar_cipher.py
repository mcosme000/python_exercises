alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

"""
identify the index of letter in alphabet.
increase the index by the shift number
 if the index is bigger than len(alphabet)
 do it like alphabet[len(alphabet) - index]
"""

size = len(alphabet) - 1

# def start_game(direction):
#     match direction:
#         case "encode": encrypt(text, shift, direction)
#         case "decode": decrypt(text, shift)
#         case _: print("Type either encode or decode to run the program")


def caesar_cypher(text, shift, direction):
    print("Running the method!")
    encrypted_word = ""

    for l in text:
        print(l)
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

caesar_cypher(text, shift, direction)
