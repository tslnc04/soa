"""
Copyright 2017 Timothy Laskoski

parser.py is the module containing
"""

from soa import token, tree, errors

class Parser():
    "Parser handles most functions related to parsing"
    def __init__(self, incoming, result_tree):
        self.incoming = incoming
        self.tree = result_tree
    
    def next_token(self):
        "next_token advances to the next token"
        tok = self.incoming[0]
        self.incoming = self.incoming[1:]

        return tok

    def peek(self):
        "peek is like next, but without advancing the buffer"
        tok = self.incoming[0]

        return tok

    def assert_token(self, token_type):
        "assert_token asserts if a token follows a type"
        tok = self.next_token()
        
        if tok is None:
            errors.print_error_and_exit("InvalidToken", "expecting " + str(token_type) + " got " + str(tok), tok["Pos"])
        
        if tok["Typ"] != token_type:
            errors.print_error_and_exit("InvalidToken", "expecting " + str(token_type) + " got " + str(tok), tok["Pos"])

        return tok

    def parse_main(self, parent):
        "parse_main is the main function for parsing"
        def return_func():
            "return_func is an inner function supposed to be anonymous"
            nonlocal parent

            tok = self.peek()

            if tok is None:
                return None

            if tok["Typ"] == token.SET:
                return self.parse_set(parent)
            elif tok["Typ"] == token.OUT:
                return self.parse_out(parent)
            elif tok["Typ"] == token.ADD:
                return self.parse_add(parent)
            elif tok["Typ"] == token.EOL:
                return self.parse_eol(parent)
            elif tok["Typ"] == token.EOF:
                return None

            return None
        return return_func

    def parse_set(self, parent):
        "parse_set adds the token onto the main tree"
        def return_func():
            "return_func is an inner function supposed to be anonymous"
            nonlocal parent

            set_tok = self.next_token()
            set_tree = tree.create_tree_with_token(set_tok, parent)
            tree.tree_append(parent, set_tree)
            
            register = self.assert_token(token.REGISTER)
            tree.add_subtree(set_tree, register)

            if self.peek()["Typ"] == token.REGISTER:
                register2 = self.next_token()
                tree.add_subtree(set_tree, register2)
            elif self.peek()["Typ"] == token.INT:
                int_tok = self.next_token()
                tree.add_subtree(set_tree, int_tok)
            else:
                errors.print_error_and_exit("InvalidToken", "expecting " + self.peek()["Typ"] + " got " + str(self.peek()), self.peek()["Pos"])

            return self.parse_main(parent)
        return return_func

    def parse_out(self, parent):
        "parse_out adds the out token to the main tree"
        def return_func():
            "return_func is an inner function supposed to be anonymous"
            nonlocal parent

            out = self.next_token()
            out_tree = tree.create_tree_with_token(out, parent)
            tree.tree_append(parent, out_tree)

            while self.peek()["Typ"] in [token.REGISTER, token.INT]:
                tok = self.next_token()
                tree.add_subtree(out_tree, tok)

            return self.parse_main(parent)
        return return_func

    def parse_add(self, parent):
        "parse_add adds the add token to the main tree"
        def return_func():
            "return_func is an inner function supposed to be anonymous"
            nonlocal parent

            add_tok = self.next_token()
            add_tree = tree.create_tree_with_token(add_tok, parent)
            tree.tree_append(parent, add_tree)
            
            register = self.assert_token(token.REGISTER)
            tree.add_subtree(add_tree, register)

            if self.peek()["Typ"] == token.REGISTER:
                register2 = self.next_token()
                tree.add_subtree(add_tree, register2)
            elif self.peek()["Typ"] == token.INT:
                int_tok = self.next_token()
                tree.add_subtree(add_tree, int_tok)
            else:
                errors.print_error_and_exit("InvalidToken", "expecting " + self.peek()["Typ"] + " got " + str(self.peek()), self.peek()["Pos"])

            return self.parse_main(parent)
        return return_func

    def parse_eol(self, parent):
        "parse_eol is a simple function basically ignoring the new line"
        def return_func():
            "return_func is an inner function supposed to be anonymous"
            nonlocal parent

            self.next_token()

            return self.parse_main(parent)
        return return_func

    def run(self):
        "run starts the state machine"
        state = self.parse_main(self.tree)
        while state:
            state = state()

def parse_soa(incoming):
    "parse_soa starts up the parser"
    result_tree = tree.create_tree(None)
    parse = Parser(incoming, result_tree)

    parse.run()

    return result_tree