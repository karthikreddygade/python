alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

'''def encrypt(original_text, shift_amount):
    cypher_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        a = shift_position % 25
        cypher_text += alphabet[a-1]
    print(cypher_text)
def decrypt(original_text , shift_amount):
    ceser_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        a = shift_position % 25
        ceser_text += alphabet[a-1]
    print(ceser_text)
'''
def ceaser(original_text , shift_amount , encoded_or_decoded):
    output_text = ""
    if encoded_or_decoded == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
           # letter == letter
            output_text += letter
        else:
            shift_position = alphabet.index(letter) + shift_amount
            a = shift_position % len(alphabet)
            output_text += alphabet[a]
    print(f"Here is the {encoded_or_decoded}d code:{output_text}")
#ceaser(text, shift, direction)
a = True
while a:
        direction = input("enter encode for encoding and decode for decoding:\n")
        text = input("Type your text:\n").lower()
        shift = int(input("Enter no.of Shifts\n"))
        ceaser(text, shift, direction)
        loop = input("do you wanna continue type yes else no\n").lower()
        if loop == "no":
            a = False
        else:
            a = True
