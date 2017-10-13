"""
__main__.py
runs code? I haven't a clue on how to use directories as modules in python
"""

import lexer
import token

code = """
set R0 1
add R0 1
out R0
"""

token.print_tokens(lexer.lex_soa(code))