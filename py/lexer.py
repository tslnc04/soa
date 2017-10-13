"""
lexer.py contains the lexer class and its associated functions
"""

class Lexer():
    "Lexer is the main class for lexing"
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0
        self.buffer = []
        self.tokens = []

    def next_char(self):
        "next moves the position over and returns the next character"
        if self.pos >= len(self.input_text):
            return chr(0)      
        
        self.pos += 1
        char = self.input_text[self.pos]
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
        if self.pos + len(expected) > len(self.input_text[self.pos:]):
            return False
        
        next_char = "".join(self.input_text[self.pos:self.pos + expected])

        return next_char == expected

    def forward(self, times):
        "forward moves the position forward and adds to the buffer times times"
        for _ in range(times):
            self.next_char()
            