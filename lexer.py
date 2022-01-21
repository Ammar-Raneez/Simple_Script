from position import *
from constants import *
from token import *
from error import IllegalCharError


# Will convert the input to tokens
class Lexer:
    # f_name -> string fileName
    # text -> string text (input)
    def __init__(self, f_name, text):
        self.f_name = f_name
        self.text = text

        # set as -1 since advance() will increment initially
        self.pos = Position(-1, 0, -1, f_name, text)
        self.current_char = None
        self.advance()

    # Traverse through the input
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    # create tokens
    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            # Ignore spaces and tabs
            if self.current_char in ' \t':
                self.advance()

            # Create tokens based on the current character
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()

            # handle invalid characters
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, '\'' + char + '\'')

        # detect EOF of tokens
        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    # create identifiers
    def make_identifier(self):
        identifier_str = ''
        pos_start = self.pos.copy()

        # allow only letters
        while self.current_char is not None and self.current_char in LETTERS:
            identifier_str += self.current_char
            self.advance()

        # token either a keyword or identifier (keywords here are SHOW and SAVE)
        tok_type = TT_KEYWORD if identifier_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, identifier_str, pos_start, self.pos)

    # create primitive numbers
    def make_number(self):
        num_str = ''
        decimal_count = 0
        pos_start = self.pos.copy()

        # Keep track of whether it's an integer or a float
        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                # Only a single decimal point is allowed for a float
                if decimal_count == 1:
                    break
                decimal_count += 1
            num_str += self.current_char
            self.advance()

        # An integer will have 0 decimal points
        if decimal_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        return Token(TT_FLOAT, float(num_str), pos_start, self.pos)
