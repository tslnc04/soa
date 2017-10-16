"""
__main__.py
runs code? I haven't a clue on how to use directories as modules in python
"""

import soa.lexer
import soa.parser
import soa.token

code = """
set R0 1
add R0 1
out R0
"""

with open("test.soa", "r") as f:
    code = f.read()
    f.close()

# TODO: IMPLEMENT AN EOF
# Just add a null byte to the end of the input text
# This causes issues where there isn't an EOL before EOF
lexed = soa.lexer.lex_soa(code)

print("----- LEXER -----\n")
soa.token.print_tokens(lexed)
print("\n----- PARSER -----\n")
parsed = soa.parser.parse_soa(lexed)
print(str(parsed).replace("'", '"').replace("...", "").replace("None", "null"))
