import string

alphabet = list(string.ascii_lowercase)

def caesar(text, shift, direction):
    result = ""

    if direction == "decode":
        shift *= -1

    for char in text:

        if char.isalpha():

            is_upper = char.isupper()
            char = char.lower()

            position = alphabet.index(char)

            new_position = (position + shift) % 26

            new_char = alphabet[new_position]

            if is_upper:
                new_char = new_char.upper()

            result += new_char

        else:
            result += char

    return result


print("=== Caesar Cipher ===")

direction = input("Type 'encode' or 'decode': ").lower()

message = input("Enter your message: ")

shift = int(input("Enter shift number: "))

output = caesar(message, shift, direction)

print(f"\nResult: {output}")