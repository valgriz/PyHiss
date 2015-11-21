import re

_alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(regular_message):
    regular_message = re.sub("[\W\d_]+", "", regular_message.strip()).lower()
    return regular_message


def demap_letter(letter): #this function takes in a latter and returns one letter less in alphabet, a --> z
    current_letter_index =  next((i for i, _letter in enumerate(_alphabet) if _letter == letter), None);
    if current_letter_index > 0:
        return _alphabet[current_letter_index-1:current_letter_index]
    else:
        return _alphabet[25:]

def decode(encrypted_message):
    return


def print_message(op, message):
    # op true = encode, op false = fasle
    if op:
        print encode(message)
    else:
        print decode(message)


def prompt():
    operation = raw_input("Do you want to encode or decode a message?\na) encode\nb) decode\n")
    global op
    global message
    if operation.lower() == "a":
        print_message(True, raw_input("Enter message to encode: "))
    elif operation.lower() == "b":
        print_message(False, raw_input("Enter message to decode: "))
        print_message(op, message)
    else:
        print "Input unrecognized, try again!"
        prompt()


prompt()
