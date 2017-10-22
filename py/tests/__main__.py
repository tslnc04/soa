"""
Copyright 2017 Timothy Laskoski

__main__.py runs the actual tests in other files
"""

import test_lexer
import test_parser
import test_interpreter

print("----- TEST SUITE -----\n")
print("TEST LEX SET", test_lexer.test_set_lexing())
print("TEST LEX OUT", test_lexer.test_out_lexing())
print("TEST LEX ADD", test_lexer.test_add_lexing())
print()
print("TEST PARSE SET", test_parser.test_set_parsing())
print("TEST PARSE OUT", test_parser.test_out_parsing())
print("TEST PARSE ADD", test_parser.test_add_parsing())
print()
print("TEST INTERPRET SET", test_interpreter.test_set_interpreting())
test_interpreter.test_out_interpreting()
print("TEST INTERPRET OUT [SHOULD SEE '0 0' ABOVE]")
print("TEST INTERPRET ADD", test_interpreter.test_set_interpreting())