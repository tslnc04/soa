"""
Copyright 2017 Timothy Laskoski

test_interpreter.py tests the interpreter
"""

import soa.interpreter
import soa.token

def test_set_interpreting():
    "Tests if the interpreter properly interprets a set"
    tokens = [
        {"Pos": 3, "Typ": soa.token.SET, "Val": "set"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "1"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    interpreted = soa.interpreter.Interpreter(parsed)
    interpreted.run()

    if interpreted.get_registry(0) == 1:
        return True

    return False

def test_out_interpreting():
    "Tests if the interpreter properly interprets an out"
    tokens = [
        {"Pos": 3, "Typ": soa.token.OUT, "Val": "out"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    soa.interpreter.interpret_soa(parsed)

def test_add_interpreting():
    "Tests if the interpreter properly interprets an add"
    tokens = [
        {"Pos": 3, "Typ": soa.token.ADD, "Val": "add"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "1"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    interpreted = soa.interpreter.Interpreter(parsed)
    interpreted.run()

    if interpreted.get_registry(0) == 1:
        return True

    return False

def test_exit_interpreting():
    "Tests if the interpreter properly interprets an exit"
    tokens = [
        {"Pos": 4, "Typ": soa.token.EXIT, "Val": "exit"},
        {"Pos": 4, "Typ": soa.token.EOF, "Val": ""}
    ]

    parsed = soa.parser.parse_soa(tokens)
    interpreted = soa.interpreter.Interpreter(parsed)
    interpreted.run()
