"""
Copyright 2017 Timothy Laskoski

test_lexer.py tests the lexer
"""


import soa.lexer
import soa.token

def test_set_lexing():
    "Tests if the lexer properly lexes a set"
    code = "set R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": soa.token.SET, "Val": "set"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_out_lexing():
    "Tests if the lexer properly lexes an out"
    code = "out R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": soa.token.OUT, "Val": "out"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_add_lexing():
    "Tests if the lexer properly lexes an add"
    code = "add R0 0"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": soa.token.ADD, "Val": "add"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_exit_lexing():
    "Tests if the lexer properly lexes an exit"
    code = "exit"
    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 4, "Typ": soa.token.EXIT, "Val": "exit"},
        {"Pos": 4, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True

    return False

def test_comment_lexing():
    "Tests if the lexer properly lexes an exit"
    code = "# This is a comment"

    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 19, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True

    return False

def test_if_lexing():
    "Tests if the lexer properly lexes an if"
    code = "if"

    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 2, "Typ": soa.token.IF, "Val": "if"},
        {"Pos": 2, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True

    return False

def test_fi_lexing():
    "Tests if the lexer properly lexes an fi"
    code = "fi"

    output = soa.lexer.lex_soa(code)

    expected = [
        {"Pos": 2, "Typ": soa.token.FI, "Val": "fi"},
        {"Pos": 2, "Typ": soa.token.EOF, "Val": ""}
    ]

    if output == expected:
        return True

    return False
