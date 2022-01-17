from parse_result import *
from constants import *
from error import InvalidSyntaxError
from node import *


class Parser:
    # tokens -> list of Tokens provided by lexer
    # token_index -> int index tracker
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

    def expr(self):
        res = ParseResult()
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

            # after an identifier the expression is expected
            expr = NumberNode(self.current_token)
            if res.error:
                return res

            return res.success(VarAssignNode(var_name, expr))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                'Expected \'SAVE\', \'SHOW\', int, float, identifier'
            ))

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

        else:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                'Invalid Keyword, identifier'
            ))
