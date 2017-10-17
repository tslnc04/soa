"""
tests.py contains the code for tests to make sure my code actually works and isn't brittle
"""

from soa import lexer

def test_set_lexing():
    "Tests if the lexer properly lexes a set"
    code = "set R0 0"
    output = lexer.lex_soa(code)

    if output[0] != {"Pos": 3, "Typ": 4, "Val": "set"}:
        return False
    if output[1] != {"Pos": 6, "Typ": 3, "Val": "R0"}:
        return False
    if output[2] != {"Pos": 8, "Typ": 7, "Val": "0"}:
        return False
    if output[3] != {"Pos": 8, "Typ": 1, "Val": ""}:
        return False
    
    return True

def test_out_lexing():
    "Tests if the lexer properly lexes an out"
    code = "out R0 0"
    output = lexer.lex_soa(code)

    if output[0] != {"Pos": 3, "Typ": 5, "Val": "out"}:
        return False
    if output[1] != {"Pos": 6, "Typ": 3, "Val": "R0"}:
        return False
    if output[2] != {"Pos": 8, "Typ": 7, "Val": "0"}:
        return False
    if output[3] != {"Pos": 8, "Typ": 1, "Val": ""}:
        return False
    
    return True

def test_add_lexing():
    "Tests if the lexer properly lexes a add"
    code = "add R0 0"
    output = lexer.lex_soa(code)

    if output[0] != {"Pos": 3, "Typ": 6, "Val": "add"}:
        return False
    if output[1] != {"Pos": 6, "Typ": 3, "Val": "R0"}:
        return False
    if output[2] != {"Pos": 8, "Typ": 7, "Val": "0"}:
        return False
    if output[3] != {"Pos": 8, "Typ": 1, "Val": ""}:
        return False
    
    return True