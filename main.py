import re


def prompt():
    print "prompt"

prompt()


def encode(regular_message):
    regular_message = re.sub("[\W\d_]+", "", regular_message.strip()).lower()
    return regular_message


def decode(encrypted_message):
    return


def print_message(op, message):
    print

#print encode("sWWWWj423!!@@@_[]()&^%$#@JMNHBGVFHRTNYJTMYRT~!@#$^*)8&^%$&<><>,,.,.765434kl~>>>*&grffeytr")
