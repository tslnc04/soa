"""
Copyright 2017 Timothy Laskoski

tests.py contains the code for tests to make sure my code actually works and isn't brittle
"""

from soa import lexer, parser, interpreter

def test_set_lexing():
    "Tests if the lexer properly lexes a set"
    code = "set R0 0"
    output = lexer.lex_soa(code)

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
    output = lexer.lex_soa(code)

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
    output = lexer.lex_soa(code)

    expected = [
        {"Pos": 3, "Typ": 6, "Val": "add"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    if output == expected:
        return True
    
    return False

def test_set_parsing():
    "Tests if the parser properly parses a set"
    tokens = [
        {"Pos": 3, "Typ": 4, "Val": "set"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    output = parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
        output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
        output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_out_parsing():
    "Tests if the parser properly parses an out"
    tokens = [
        {"Pos": 3, "Typ": 5, "Val": "out"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    output = parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
        output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
        output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_add_parsing():
    "Tests if the parser properly parses an add"
    tokens = [
        {"Pos": 3, "Typ": 6, "Val": "add"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "0"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    output = parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
        output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
        output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_set_interpreting():
    "Tests if the interpreter properly parses a set"
    tokens = [
        {"Pos": 3, "Typ": 4, "Val": "set"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "1"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    parsed = parser.parse_soa(tokens)
    interpreted = interpreter.Interpreter(parsed)
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

    parsed = parser.parse_soa(tokens)
    interpreter.interpret_soa(parsed)

def test_add_interpreting():
    "Tests if the interpreter properly parses an add"
    tokens = [
        {"Pos": 3, "Typ": 6, "Val": "add"},
        {"Pos": 6, "Typ": 3, "Val": "R0"},
        {"Pos": 8, "Typ": 7, "Val": "1"},
        {"Pos": 8, "Typ": 1, "Val": ""}
    ]

    parsed = parser.parse_soa(tokens)
    interpreted = interpreter.Interpreter(parsed)
    interpreted.run()

    if interpreted.get_registry(0) == 1:
        return True

    return False