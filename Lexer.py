from Token import Token

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

DIGITS = '1234567890'
SYMBOLS = [
    ['+', TT_PLUS], ['-', TT_MINUS], ['*', TT_MUL],
    ['/', TT_DIV], ['(', TT_LPAREN], [')', TT_RPAREN]
]

        

class Lexer:
    def __init__(self, _text) -> None:
        self.text = _text
        self.current_char = None
        self.index = -1
        self.advance()
        
    def advance(self):
        self.index += 1
        if self.index < len(self.text):
            self.current_char = self.text[self.index]
        else:
            self.current_char = None
            
    def get_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                    self.advance() 
            elif self.current_char in DIGITS:
                tokens.append(self.parse_number())
            elif any(self.current_char in s for s in SYMBOLS): 
                for symbol in SYMBOLS:
                    if self.current_char == symbol[0]:
                        tokens.append(Token(symbol[1]))
                        self.advance()
            else:
                self.advance()
                return [], 'Invalid character'
        return tokens, None
    
    
    def parse_number(self):
        numstr = ''
        dotcount = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if (self.current_char == '.'):
                if (dotcount == 1): break
                dotcount += 1
                numstr += '.'
            else: numstr += self.current_char
            self.advance()
        
        if (dotcount == 0):
            return Token(TT_INT, int(numstr))
        else:
            return Token(TT_FLOAT, float(numstr));
        
        