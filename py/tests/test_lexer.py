"""
Copyright 2017 Timothy Laskoski

test_lexer.py tests the lexer
"""


import soa.lexer

def test_set_lexing():
    "Tests if the lexer properly lexes a set"
    code = "set R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": 4, "Val": "set"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_out_lexing():
    "Tests if the lexer properly lexes an out"
    code = "out R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": 5, "Val": "out"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_add_lexing():
    "Tests if the lexer properly lexes an add"
    code = "add R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": 6, "Val": "add"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False
