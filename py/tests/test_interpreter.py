"""
Copyright 2017 Timothy Laskoski

test_interpreter.py tests the interpreter
"""

import soa.interpreter

def test_set_interpreting():
    "Tests if the interpreter properly parses a set"
    tokens = [
        {"Pos": 3, "Typ": 4, "Val": "set"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "1"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    interpreted = soa.interpreter.Interpreter(parsed)
    interpreted.run()

    if interpreted.get_registry(0) == 1:
        return True

    return False

def test_out_interpreting():
    "Tests if the interpreter properly parses an out"
    tokens = [
        {"Pos": 3, "Typ": 5, "Val": "out"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    soa.interpreter.interpret_soa(parsed)

def test_add_interpreting():
    "Tests if the interpreter properly parses an add"
    tokens = [
        {"Pos": 3, "Typ": 6, "Val": "add"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "1"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    interpreted = soa.interpreter.Interpreter(parsed)
    interpreted.run()

    if interpreted.get_registry(0) == 1:
        return True

    return False
