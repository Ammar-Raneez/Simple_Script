from position import *
from constants import *
from tokens import *
from error import IllegalCharError, ExpectedCharError


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

            # An identifier can only start with letters or an underscore
            elif self.current_char in LETTERS + '_':
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(self.make_minus_or_arrow())
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
            elif self.current_char == '!':
                token, error = self.make_not_equals()
                if error:
                    return [], error
                tokens.append(token)
            elif self.current_char == '=':
                token, error = self.make_equals()
                if error:
                    return [], error
                tokens.append(token)
            elif self.current_char == '<':
                token, error = self.make_less_than()
                if error:
                    return [], error
                tokens.append(token)
            elif self.current_char == '>':
                token, error = self.make_greater_than()
                if error:
                    return [], error
                tokens.append(token)
            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA, pos_start=self.pos))
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

        # allow letters, digits and underscores
        while self.current_char is not None and self.current_char in LETTERS + DIGITS + '_':
            identifier_str += self.current_char
            self.advance()

        identifier_str = identifier_str.upper()

        # token either a keyword or identifier (keywords here are SHOW and VAR)
        tok_type = TT_KEYWORD if identifier_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, identifier_str, pos_start, self.pos)

    # create tokens for !=
    def make_not_equals(self):
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            return Token(TT_NE, pos_start=pos_start, pos_end=self.pos), None

        self.advance()
        return None, ExpectedCharError(pos_start, self.pos, "'=' (after '!')")

    # create tokens for = and ==
    def make_equals(self):
        tok_type = TT_EQ
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_EE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos), None

    # create tokens for < and <=
    def make_less_than(self):
        token_type = TT_LT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_LTE

        return Token(token_type, pos_start=pos_start, pos_end=self.pos), None

    # create tokens for > and >=
    def make_greater_than(self):
        token_type = TT_GT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_GTE

        return Token(token_type, pos_start=pos_start, pos_end=self.pos), None

    # create primitive number tokens
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

    def make_minus_or_arrow(self):
        tok_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '>':
            self.advance()
            tok_type = TT_ARROW

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)
