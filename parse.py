from parse_result import *
from constants import *
from error import InvalidSyntaxError
from node import *


class Parser:
    # tokens -> list of Tokens provided by lexer
    # token_index -> int index tracker
    # current_token -> currently referenced token
    def __init__(self, tokens):
        self.current_token = None
        self.tokens = tokens
        self.token_index = -1
        self.advance()

    # Traverse the tokens
    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token

    # parse the expression
    def parse(self):
        res = self.expr()
        return res

    # create respective Nodes based on token type
    def expr(self):
        res = ParseResult()

        # Variable assignment
        if self.current_token.matches(TT_KEYWORD, 'SAVE'):
            res.register_advancement()
            self.advance()

            # once the keyword is advanced only an identifier is accepted
            if self.current_token.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_token.pos_start, self.current_token.pos_end,
                    'Expected identifier'
                ))

            # valid identifier
            var_name = self.current_token
            res.register_advancement()
            self.advance()

            # after an identifier only the value is accepted
            expr = NumberNode(self.current_token)
            if res.error:
                return res

            return res.success(VarAssignNode(var_name, expr))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                'Expected \'SAVE\', \'SHOW\', int, float, identifier'
            ))

        # variable access
        elif self.current_token.matches(TT_KEYWORD, 'SHOW'):
            res.register_advancement()
            self.advance()

            # once the keyword is advanced only an identifier is accepted
            if self.current_token.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_token.pos_start, self.current_token.pos_end,
                    'Expected \'SAVE\', \'SHOW\', int, float, identifier'
                ))

            return res.success(VarAccessNode(self.current_token))

        # invalid keyword
        else:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                'Invalid Keyword, identifier'
            ))
