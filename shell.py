from Lexer import Lexer

def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.get_tokens()
    return tokens, errors


while True:
    text = input('Basic > ')
    result, errors = run(text)
    if not errors:
        print(result)
    else: print(errors)
