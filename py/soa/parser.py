"""
parser.py is the module containing
"""

import token
import tree

class Parser():
    "Parser handles most functions related to parsing"
    def __init__(self):
        self.incoming = {}
        self.tree = {}
        self.buffer = []
    
    def next_token(self):
        "next_token advances to the next token"
        if (len(self.buffer) != 0):
            tok = self.buffer[0]
            self.buffer = self.buffer[1:]
            return tok

        tok = self.incoming
        self.incoming = {}

        return tok

    def peek(self):
        "peek is like next, but without advancing the buffer"
        if (len(self.buffer) != 0):
            return self.buffer[0]

        tok = self.incoming
        self.incoming = {}

        return tok

    def assert_token(self, token_type):
        "assert_token asserts if a token follows a type"
        tok = self.next()
        
        if tok is None:
            print("EXPEXTING", token_type, "GOT NOTHING")
        
        if tok.Typ != token_type:
            print("EXPECTING", token_type, "GOT", tok)

        return tok

    def parse_main(self, parent):
        "parse_main is the main function for parsing"
        tok = self.peek()

        if tok is None:
            return None

        if tok.Typ == SET:
            return self.parse_set(parent)
        elif tok.Typ == OUT:
            return self.parse_out(parent)
        elif tok.Typ == ADD:
            return self.parse_add(parent)
        elif tok.Typ == REGISTER:
            return self.parse_register(parent)
        elif tok.Typ == INT:
            return self.parse_int(parent)
        elif tok.Typ == EOL:
            return self.parse_eol(parent)
        elif tok.Typ == EOF:
            return None

        return None

    def parse_set(self, parent):
        "parse_set adds the token onto the main tree"
        set_tok = self.next_token()
        set_tree = tree.create_tree_with_token(set_tok, parent)
        tree.tree_append(parent, set_tree)
        
        register = self.assert_token(token.REGISTER)
        parent, _ = tree.add_subtree(set_tree, register)

        if self.peek().Typ == token.REGISTER:
            register2 = self.next_token()
            parent, _ = tree.add_subtree(set_tree, register2)
