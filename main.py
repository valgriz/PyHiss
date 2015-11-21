import re


def encode(regular_message):
    regular_message = re.sub("[\W\d_]+", "", regular_message.strip()).lower()
    return regular_message


def decode(encrypted_message):
    return


def print_message(op, message):
    #op true = encode, op false = fasle
    if op:
        print encode(message)
    else:
        print decode (message)


def prompt():
    operation = raw_input("Do you want to encode or decode a message?\na) encode\nb) decode\n")
    if operation.lower() == "a":
        op = True
        message = raw_input("Enter message to encode: ")
    elif operation.lower() == "b":
        op = False
        message = raw_input("Enter message to decode: ")
    else:
        print "Input unrecognized, try again!"
        prompt()
    print_message(op, message)

prompt()






#print encode("sWWWWj423!!@@@_[]()&^%$#@JMNHBGVFHRTNYJTMYRT~!@#$^*)8&^%$&<><>,,.,.765434kl~>>>*&grffeytr")
