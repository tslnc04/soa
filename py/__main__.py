"""
__main__.py
runs code? I haven't a clue on how to use directories as modules in python
"""

import soa.lexer
import soa.parser
import soa.token
import soa.tests
import soa.interpreter

code = """
set R0 1
add R0 1
out R0
"""

print("----- TEST SUITE -----\n")
print("TEST LEX SET", soa.tests.test_set_lexing())
print("TEST LEX OUT", soa.tests.test_out_lexing())
print("TEST LEX ADD", soa.tests.test_add_lexing())

with open("test.soa", "r") as f:
    code = f.read()
    f.close()
    
lexed = soa.lexer.lex_soa(code)

print("\n----- LEXER -----\n")
soa.token.print_tokens(lexed)
print("\n----- PARSER -----\n")
parsed = soa.parser.parse_soa(lexed)
print(str(parsed).replace("'", '"').replace("...", "").replace("None", "null"))
print("\n----- INTERPRETER -----\n")
soa.interpreter.interpret_soa(parsed)
