def encode(regular_message):
    return


def decode(encrypted_message):
    return


def print_message(op, message):
    #op true = encode, op false = fasle
    if op == True:
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






