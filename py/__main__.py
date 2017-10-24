"""
Copyright 2017 Timothy Laskoski

__main__.py runs the test suite for now
"""

import soa.lexer
import soa.parser
import soa.interpreter

code = """
if R0 0
set R0 10
fi
"""

if not code:
    with open("test.soa", "r") as f:
        code = f.read()
        f.close() 

lexed = soa.lexer.lex_soa(code)

print("\n----- LEXER -----\n")
print(str(lexed).replace("'", '"').replace("...", "").replace("None", "null"))
# soa.token.print_tokens(lexed)
print("\n----- PARSER -----\n")
parsed = soa.parser.parse_soa(lexed)
print(str(parsed).replace("'", '"').replace("...", "").replace("None", "null"))
print("\n----- INTERPRETER -----\n")
soa.interpreter.interpret_soa(parsed)
