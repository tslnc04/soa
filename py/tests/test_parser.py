"""
Copyright 2017 Timothy Laskoski

test_parser.py tests the parser
"""

import soa.parser
import soa.token

def test_set_parsing():
    "Tests if the parser properly parses a set"
    tokens = [
        {"Pos": 3, "Typ": soa.token.SET, "Val": "set"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    output = soa.parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
            output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
            output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_out_parsing():
    "Tests if the parser properly parses an out"
    tokens = [
        {"Pos": 3, "Typ": soa.token.OUT, "Val": "out"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    output = soa.parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
            output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
            output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_add_parsing():
    "Tests if the parser properly parses an add"
    tokens = [
        {"Pos": 3, "Typ": soa.token.ADD, "Val": "add"},
        {"Pos": 6, "Typ": soa.token.REGISTER, "Val": "R0"},
        {"Pos": 8, "Typ": soa.token.INT, "Val": "0"},
        {"Pos": 8, "Typ": soa.token.EOF, "Val": ""}
    ]

    output = soa.parser.parse_soa(tokens)

    if (output["Sub"][0]["Tok"] == tokens[0] and 
            output["Sub"][0]["Sub"][0]["Tok"] == tokens[1] and 
            output["Sub"][0]["Sub"][1]["Tok"] == tokens[2]):
        return True

    return False

def test_exit_parsing():
    "Tests if the parser properly parses an exit"
    tokens = [
        {"Pos": 4, "Typ": soa.token.EXIT, "Val": "exit"},
        {"Pos": 4, "Typ": soa.token.EOF, "Val": ""}
    ]

    output = soa.parser.parse_soa(tokens)

    if output["Sub"][0]["Tok"] == tokens[0]:
        return True

    return False
