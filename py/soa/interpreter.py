"""
interpreter.py contains the interpreter class and its associated methods
"""

from soa import token

def get_register_value(register_tree):
    "get_int_value uses a tree to find the value of the register"
    register_token = register_tree["Tok"]
    register_value = register_token["Val"][1:]

    return int(register_value)

def get_int_value(int_tree):
    "get_int_value uses a tree to find the integer value of the token"
    int_token = int_tree["Tok"]
    int_value = int_token["Val"]

    return int(int_value)

def get_tree_type(token_tree):
    "get_tree_type returns the token type of the token in a tree"
    token_token = token_tree["Tok"]
    token_type = token_token["Typ"]

    return token_type

class Interpreter():
    "The Interpreter carries all of the methods related to the interpreter"
    def __init__(self, parse_tree):
        self.tree = parse_tree
        self.registry = []

    def get_registry(self, index):
        "get_registry gets the value of a spot on the registry"
        if index >= len(self.registry):
            print("INDEX OUT OF RANGE", index)
            exit(-1)

        return self.registry[index]

    def set_registry(self, index, value):
        "set_registry sets the value at a spot on the register"
        if not isinstance(value, x):
            print("REGISTERS MUST BE INTEGERS", value)
            exit(-1)
        
        self.registry[index] = value

    def interpret_set(self, set_tree):
        "interpret_set adds functionality to the set keyword"
        set_register = get_register_value(set_tree["Sub"][0])
        
        if get_tree_type(set_tree["Sub"][1]) == token.INT:
            set_value = get_int_value(set_tree["Sub"][1])
            self.set_registry(set_register, set_value)
        elif get_tree_type(set_tree["Sub"][1]) == token.REGISTER:
            value_register = get_register_value(set_tree["Sub"][1])
            self.set_registry(set_register, self.get_registry(value_register))

    def interpret_add(self, add_tree):
        "interpret_add adds two values together"
        add_register = get_register_value(add_tree["Sub"][0])
        current_value = self.get_registry(add_register)

        if get_tree_type(add_tree["Sub"][1]) == token.INT:
            add_value = get_int_value(add_tree["Sub"][1])
            self.set_registry(add_register, add_value + current_value)
        elif get_tree_type(add_tree["Sub"][1]) == token.REGISTER:
            value_register = get_register_value(add_tree["Sub"][1])
            value_register_value = self.get_registry(value_register)
            self.set_registry(add_register, value_register_value + current_value)