"""
lexer.py contains the lexer class and its associated functions
"""

from soa import token

EOF_CHAR = chr(0)

class Lexer():
    "Lexer is the main class for lexing"
    def __init__(self, input_text):
        self.input_text = input_text + EOF_CHAR
        self.pos = 0
        self.buffer = []
        self.tokens = []

    def next_char(self):
        "next moves the position over and returns the next character"
        if self.pos >= len(self.input_text):
            return chr(0)      
        
        char = self.input_text[self.pos]
        self.pos += 1
        self.buffer.append(char)

        return char
    
    def backup(self):
        "backup removes the last character from the buffer and sets the position back 1"
        self.pos -= 1
        self.buffer = self.buffer[:-1]

    def ignore(self):
        "ignore resets the buffer"
        self.buffer = []

    def peek(self):
        "peek returns the next character without moving the position or addng to the buffer"
        char = self.next_char()
        self.backup()

        return char
    
    def emit_with_value(self, token_type, value):
        "emitWithValue adds a new token to the tokens array"
        self.tokens.append({
            "Pos": self.pos,
            "Typ": token_type,
            "Val": value
        })
    
    def emit(self, token_type):
        "emit uses the buffer when adding to the tokens array"
        self.emit_with_value(token_type, "".join(self.buffer))

    def follow(self, expected):
        "follow determines if the expected string matches the input_text"
        if len(expected) > len(self.input_text[self.pos:]):
            return False
        
        got = "".join(self.input_text[self.pos:self.pos + len(expected)])

        return got == expected

    def forward(self, times):
        "forward moves the position forward and adds to the buffer times times"
        for _ in range(times):
            self.next_char()

    def lex_main(self):
        "lex_main is the main loop for the lexer"
        while True:
            next_char = self.peek()
            
            if self.follow("set"):
                return self.lex_set
            elif self.follow("out"):
                return self.lex_out
            elif self.follow("add"):
                return self.lex_add
            
            if token.is_eol(next_char):
                return self.lex_eol

            if next_char == EOF_CHAR:
                self.ignore()
                self.emit(token.EOF)
                break
                
            self.next_char()

    def lex_values(self):
        "lex_values lexes registers and ints"
        while True:
            next_char = self.peek()

            if next_char == "R":
                return self.lex_register

            if token.is_digit(next_char):
                return self.lex_int

            if token.is_eol(next_char):
                return self.lex_eol

            if next_char == EOF_CHAR:
                self.ignore()
                self.emit(token.EOF)
                break
            
            self.next_char()
    
    def lex_register(self):
        "lex_register produces a register token"
        self.ignore()
        self.next_char()

        x = self.peek()
        while token.is_digit(x):
            self.next_char()
            x = self.peek()
        
        self.emit(token.REGISTER)

        return self.lex_values

    def lex_set(self):
        "lex_set produces a set token"
        self.ignore()
        self.forward(3)
        self.emit(token.SET)

        return self.lex_values

    def lex_out(self):
        "lex_out produces an out token"
        self.ignore()
        self.forward(3)
        self.emit(token.OUT)

        return self.lex_values

    def lex_add(self):
        "lex_add produces an add token"
        self.ignore()
        self.forward(3)
        self.emit(token.ADD)

        return self.lex_values

    def lex_int(self):
        "lex_int produces an int token"
        self.ignore()

        x = self.peek()
        while token.is_digit(x):
            self.next_char()
            x = self.peek()
        
        self.emit(token.INT)

        return self.lex_values

    def lex_eol(self):
        "lex_eol produces an eol token"
        self.ignore()

        if self.next_char() == "\r":
            self.next_char()
        
        self.emit(token.EOL)

        return self.lex_main

    def run(self):
        "run starts up the lexer loop"
        state = self.lex_main()
        while state:
            state = state()

def lex_soa(input_text):
    "lex_soa creates the lexer and starts it"
    lexer = Lexer(input_text)
    lexer.run()
    return lexer.tokens
