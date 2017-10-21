"""
interpreter.py contains the interpreter class and its associated methods
"""

from soa import token, errors

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
    "Interpreter carries all of the methods related to the interpreter"
    def __init__(self, parse_tree):
        self.tree = parse_tree
        self.registry = [0] * 1000
        self._subtree_pos = 0

    def get_next_subtree(self):
        "get_next_subtree gets the next subtree for use in interpret_main"
        if self._subtree_pos == len(self.tree["Sub"]):
            return None
        
        return_tree = self.tree["Sub"][self._subtree_pos]
        self._subtree_pos += 1

        return return_tree

    def get_registry(self, index):
        "get_registry gets the value of a spot on the registry"
        if index >= len(self.registry):
            errors.print_error_and_exit("InvalidRegister", "expecting " + str(len(self.registry)) + "< got " + str(index), 0)

        return self.registry[index]

    def set_registry(self, index, value):
        "set_registry sets the value at a spot on the register"
        if not isinstance(value, int):
            errors.print_error_and_exit("InvalidType", "expecting int, got " + str(type(value)), 0)
        elif not isinstance(index, int):
            errors.print_error_and_exit("InvalidRegister", "expecting R<int>, got R<" + str(type(value)) + ">", 0)

        if index >= len(self.registry):
            errors.print_error_and_exit("InvalidRegister", "expecting " + str(len(self.registry)) + "< got " + str(index), 0)

        self.registry[index] = value

    def interpret_set(self, set_tree):
        "interpret_set adds functionality to the set keyword"
        def inner_function():
            "inner_function exists due to python not allowing anonymous functions"
            nonlocal set_tree

            set_register = get_register_value(set_tree["Sub"][0])
            
            if get_tree_type(set_tree["Sub"][1]) == token.INT:
                set_value = get_int_value(set_tree["Sub"][1])
                self.set_registry(set_register, set_value)
            elif get_tree_type(set_tree["Sub"][1]) == token.REGISTER:
                value_register = get_register_value(set_tree["Sub"][1])
                self.set_registry(set_register, self.get_registry(value_register))
            
            return self.interpret_main
        return inner_function

    def interpret_add(self, add_tree):
        "interpret_add adds two values together"
        def inner_function():
            "inner_function exists due to python not allowing anonymous functions"
            nonlocal add_tree

            add_register = get_register_value(add_tree["Sub"][0])
            current_value = self.get_registry(add_register)

            if get_tree_type(add_tree["Sub"][1]) == token.INT:
                add_value = get_int_value(add_tree["Sub"][1])
                self.set_registry(add_register, add_value + current_value)
            elif get_tree_type(add_tree["Sub"][1]) == token.REGISTER:
                value_register = get_register_value(add_tree["Sub"][1])
                value_register_value = self.get_registry(value_register)
                self.set_registry(add_register, value_register_value + current_value)

            return self.interpret_main
        return inner_function

    def interpret_out(self, out_tree):
        "interpret_out prints out values"
        def inner_function():
            "inner_function exists due to python not allowing anonymous functions"
            nonlocal out_tree

            to_print = []
            for subtoken in out_tree["Sub"]:
                if get_tree_type(subtoken) == token.INT:
                    token_value = self.get_registry(get_int_value(subtoken))
                    to_print.append(str(token_value))
                elif get_tree_type(subtoken) == token.REGISTER:
                    token_value = self.get_registry(get_register_value(subtoken))
                    to_print.append(str(token_value))

            print(" ".join(to_print))
            return self.interpret_main
        return inner_function

    def interpret_main(self):
        "interpret_main is the loop that calls functions to actually interpret parts of code"
        while True:
            subtree = self.get_next_subtree()

            if subtree is None:
                return None
            
            if get_tree_type(subtree) == token.SET:
                return self.interpret_set(subtree)
            elif get_tree_type(subtree) == token.OUT:
                return self.interpret_out(subtree)
            elif get_tree_type(subtree) == token.ADD:
                return self.interpret_add(subtree)
            
            return None
    
    def run(self):
        "run starts the state machine"
        state = self.interpret_main
        while state:
            state = state()

def interpret_soa(parse_tree):
    "interpret_soa starts interpreting the parse tree"
    interpreter = Interpreter(parse_tree)

    interpreter.run()