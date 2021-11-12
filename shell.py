from Lexer import Lexer
import sys
import os


def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.get_tokens()
    return tokens, errors


with open(os.path.join(sys.path[0], "code.txt"), "r") as f:
    text = f.read()
    # text = input('Basic > ')
    result, errors = run(text)
    if not errors:
        print(result)
    else:
        print(errors)
