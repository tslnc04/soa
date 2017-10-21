"""
Copyright 2017 Timothy Laskoski

__main__.py runs the test suite for now
"""

import soa.tests

print("----- TEST SUITE -----\n")
print("TEST LEX SET", soa.tests.test_set_lexing())
print("TEST LEX OUT", soa.tests.test_out_lexing())
print("TEST LEX ADD", soa.tests.test_add_lexing())
print()
print("TEST PARSE SET", soa.tests.test_set_parsing())
print("TEST PARSE OUT", soa.tests.test_out_parsing())
print("TEST PARSE ADD", soa.tests.test_add_parsing())
print()
print("TEST INTERPRET SET", soa.tests.test_set_interpreting())
soa.tests.test_out_interpreting()
print("TEST INTERPRET OUT [SHOULD SEE '0 0' ABOVE]")
print("TEST INTERPRET ADD", soa.tests.test_set_interpreting())

# with open("test.soa", "r") as f:
#     code = f.read()
#     f.close() 
# lexed = soa.lexer.lex_soa(code)

# print("\n----- LEXER -----\n")
# soa.token.print_tokens(lexed)
# print("\n----- PARSER -----\n")
# parsed = soa.parser.parse_soa(lexed)
# print(str(parsed).replace("'", '"').replace("...", "").replace("None", "null"))
# print("\n----- INTERPRETER -----\n")
# soa.interpreter.interpret_soa(parsed)
