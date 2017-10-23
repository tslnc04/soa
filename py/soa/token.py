"""
Copyright 2017 Timothy Laskoski

token.py contains the code for token types and some basic character tests
"""

ERROR = 0
EOF = 1
EOL = 2

REGISTER = 3
INT = 4

SET = 5
OUT = 6
ADD = 7
EXIT = 8
IF = 9
FI = 10

TOKEN_NAMES = [
    "error",
    "eof",
    "eol",
    "register",
    "int",
    "set",
    "out",
    "add",
    "exit",
    "if",
    "fi"
]

def is_eol(char):
    "is_eol tests if a character denotes an end of line"
    return char == "\n" or char == "\r"

def is_digit(char):
    "is_digit tests is a given character is a numerical digit"
    return (ord(char) in [(ord("0") + x) for x in range(10)] or ord(char) == ord("-"))

def print_tokens(tokens):
    "print_tokens is a prettier way of printing the tokens array"
    for token in tokens:
        print("POS", token["Pos"], "TYP", token["Typ"], "VAL", token["Val"])
        