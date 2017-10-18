"""
errors.py is some error handling for the interpreter and eventually all other portions
"""

class Error():
    "Error is the class that holds error data and some methods that are related"
    def __init__(self, error_type, message, pos):
        "__init__ uses a type, message, and pos to create and error"
        self.error_type = error_type
        self.message = message
        self.pos = pos
    
    def print_error(self):
        "print_error prints the message and pos but does not exit"
        print(self.error_type + ":", self.message, "at position", self.pos)

    def print_and_exit(self):
        "print_and_exit prints the message and pos then exits the program"
        self.print_error()
        exit(-1)