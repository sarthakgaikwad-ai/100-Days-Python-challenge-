alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#sarthak +2
def encrypt(original_text,shift_amount):
    cipher_text=""#u
    for letter in original_text:
       shifted_position = alphabet.index(letter)+shift_amount#19+2=21
       cipher_text += alphabet[shifted_position]#u

    print(f"The encoded result is :{cipher_text}")

encrypt(original_text=text,shift_amount=shift)
