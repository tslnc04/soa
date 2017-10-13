"""
parser.py is the module containing
"""

class Parser():
    "Parser handles most functions related to parsing"
    def __init__(self):
        self.incoming = {}
        self.tree = {}
        self.buffer = []
    
    def next_token(self):
        "next_token advances to the next token"
        if (len(self.buffer) != 0):
            token = self.buffer[0]
            self.buffer = self.buffer[1:]
            return token

        token = self.incoming
        self.incoming = {}

        return token

    def peek(self):
        "peek is like next, but without advancing the buffer"
        if (len(self.buffer) != 0):
            return self.buffer[0]

        token = self.incoming
        self.incoming = {}

        return token

    def assert_token(self, token_type):
        "asserts if a token follows a type"
        token = self.next()
        
        if token is None:
            print("EXPEXTING", token_type, "GOT NOTHING")
        
        if token.Typ != token_type:
            print("EXPECTING", token_type, "GOT", token)

        return token