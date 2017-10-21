"""
Copyright 2017 Timothy Laskoski

errors.py is some error handling for the lexer, parser, and interpreter
"""

def print_error(error_type, message, pos):
    "print_error prints the message and pos but does not exit"
    print(error_type + ":", message, "at position", pos)

def print_error_and_exit(error_type, message, pos):
    "print_and_exit prints the message and pos then exits the program"
    print_error(error_type, message, pos)
    exit(-1)