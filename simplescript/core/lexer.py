"""Lexical analyzer (tokenizer) for SimpleScript.

This module provides the Lexer class that converts raw source code text
into a sequence of tokens for the parser to consume.
"""

from typing import List, Tuple, Optional
from simplescript.tokens.position import Position
from simplescript.tokens.token import Token
from simplescript.core.constants import (
    DIGITS, LETTERS, KEYWORDS,
    TT_INT, TT_FLOAT, TT_STRING, TT_PLUS, TT_MINUS, TT_MUL, TT_DIV,
    TT_POW, TT_LPAREN, TT_RPAREN, TT_EE, TT_EQ, TT_NE, TT_LT, TT_GT,
    TT_LTE, TT_GTE, TT_EOF, TT_IDENTIFIER, TT_KEYWORD, TT_COMMA, TT_ARROW,
)
from simplescript.errors.errors import IllegalCharError, ExpectedCharError, Error


class Lexer:
    """Converts source code text into a sequence of tokens.

    The lexer performs lexical analysis by scanning through the input text
    character by character, grouping characters into meaningful tokens such
    as numbers, strings, identifiers, keywords, and operators.

    Args:
        f_name: The source file name (used for error reporting).
        text: The source code text to tokenize.

    Attributes:
        f_name (str): Source file name.
        text (str): Source code text.
        pos (Position): Current position in the source text.
        current_char (Optional[str]): Character at the current position.

    Example:
        >>> lexer = Lexer('<stdin>', 'VAR x = 10 + 5')
        >>> tokens, error = lexer.make_tokens()
    """

    def __init__(self, f_name: str, text: str) -> None:
        self.f_name = f_name
        self.text = text
        self.pos = Position(-1, 0, -1, f_name, text)
        self.current_char: Optional[str] = None
        self.advance()

    def advance(self) -> None:
        """Advance the position to the next character in the source text."""
        self.pos.advance(self.current_char)
        self.current_char = (
            self.text[self.pos.index] if self.pos.index < len(self.text) else None
        )

    def make_tokens(self) -> Tuple[List[Token], Optional[Error]]:
        """Tokenize the entire source text.

        Scans through the input text and produces a list of tokens.
        The list always ends with an EOF token on success.

        Returns:
            A tuple of (tokens, error). On success, error is None.
            On failure, tokens is an empty list and error describes
            the problem.
        """
        tokens: List[Token] = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS + '_':
                tokens.append(self.make_identifier())
            elif self.current_char == '"' or self.current_char == "'":
                tokens.append(self.make_string())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                token, error = self.make_minus_or_arrow()
                if error:
                    return [], error
                tokens.append(token)
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
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, '\'' + char + '\'')

        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_identifier(self) -> Token:
        """Tokenize an identifier or keyword.

        Reads a sequence of letters, digits, and underscores, then checks
        if the result matches a reserved keyword.

        Returns:
            A KEYWORD token if the identifier matches a keyword,
            otherwise an IDENTIFIER token.
        """
        identifier_str = ''
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in LETTERS + DIGITS + '_':
            identifier_str += self.current_char
            self.advance()

        identifier_str = identifier_str.upper()
        tok_type = TT_KEYWORD if identifier_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, identifier_str, pos_start, self.pos)

    def make_string(self) -> Token:
        """Tokenize a string literal with escape character support.

        Supports both single and double quoted strings. Handles escape
        sequences: ``\\n`` (newline), ``\\t`` (tab), ``\\\\`` (backslash),
        ``\\"`` (double quote), ``\\'`` (single quote).

        Returns:
            A STRING token containing the processed string value.
        """
        string = ''
        pos_start = self.pos.copy()
        escape_character = False
        quote_char = self.current_char
        self.advance()

        escape_characters = {
            'n': '\n',
            't': '\t',
        }

        while self.current_char is not None and (self.current_char != quote_char or escape_character):
            if escape_character:
                string += escape_characters.get(self.current_char, self.current_char)
                escape_character = False
            else:
                if self.current_char == '\\':
                    escape_character = True
                else:
                    string += self.current_char
            self.advance()

        self.advance()
        return Token(TT_STRING, string, pos_start, self.pos)

    def make_not_equals(self) -> Tuple[Optional[Token], Optional[Error]]:
        """Tokenize the not-equals operator (!=).

        Returns:
            A tuple of (NE token, None) on success, or (None, error)
            if '=' does not follow '!'.
        """
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            return Token(TT_NE, pos_start=pos_start, pos_end=self.pos), None

        self.advance()
        return None, ExpectedCharError(pos_start, self.pos, "'=' (after '!')")

    def make_equals(self) -> Tuple[Token, None]:
        """Tokenize the assignment (=) or equality (==) operator.

        Returns:
            A tuple of (EQ or EE token, None).
        """
        tok_type = TT_EQ
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_EE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos), None

    def make_less_than(self) -> Tuple[Token, None]:
        """Tokenize the less-than (<) or less-than-or-equal (<=) operator.

        Returns:
            A tuple of (LT or LTE token, None).
        """
        token_type = TT_LT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_LTE

        return Token(token_type, pos_start=pos_start, pos_end=self.pos), None

    def make_greater_than(self) -> Tuple[Token, None]:
        """Tokenize the greater-than (>) or greater-than-or-equal (>=) operator.

        Returns:
            A tuple of (GT or GTE token, None).
        """
        token_type = TT_GT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            token_type = TT_GTE

        return Token(token_type, pos_start=pos_start, pos_end=self.pos), None

    def make_number(self) -> Token:
        """Tokenize a numeric literal (integer or float).

        Reads digits and at most one decimal point. If no decimal point
        is found, produces an INT token; otherwise a FLOAT token.

        Returns:
            An INT or FLOAT token with the parsed numeric value.
        """
        num_str = ''
        decimal_count = 0
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if decimal_count == 1:
                    break
                decimal_count += 1
            num_str += self.current_char
            self.advance()

        if decimal_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        return Token(TT_FLOAT, float(num_str), pos_start, self.pos)

    def make_minus_or_arrow(self) -> Tuple[Token, None]:
        """Tokenize a minus (-) or arrow (->) operator.

        Returns:
            A tuple of (MINUS or ARROW token, None).
        """
        tok_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '>':
            self.advance()
            tok_type = TT_ARROW

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos), None
