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
        if not res.error and (self.current_token.type != TT_EOF and self.current_token.type != TT_IDENTIFIER):
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                "Expected '+', '-', '*', '/', '^', '==', '!=', '<', '>', <=', '>=', 'AND' or 'OR'"
            ))
        return res

    # handle simple atomic parsing
    def atom(self):
        res = ParseResult()
        token = self.current_token

        # If integer or float return a NumberNode of that token
        if token.type in (TT_INT, TT_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(token))

        # handle expressions within parentheses
        elif token.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error:
                return res
            if self.current_token.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_token.pos_start, self.current_token.pos_end,
                    "Expected ')'"
                ))

        return res.failure(InvalidSyntaxError(
            token.pos_start, token.pos_end,
            "Expected int, float, '+', '-' or '('"
        ))

    # handle power operation parsing
    def power(self):
        return self.bin_op(self.atom, (TT_POW,), self.factor)

    # handle factor parsing
    def factor(self):
        res = ParseResult()
        token = self.current_token

        if token.type in (TT_PLUS, TT_MINUS):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(token, factor))

        return self.power()

    # handle term parsing
    def term(self):
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    # handle arithmetic expression parsing
    def arith_expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    # handle comparison expression parsing
    def comp_expr(self):
        res = ParseResult()

        if self.current_token.matches(TT_KEYWORD, 'NOT'):
            operator_token = self.current_token
            res.register_advancement()
            self.advance()
            node = res.register(self.comp_expr())
            if res.error:
                return res
            return res.success(UnaryOpNode(operator_token, node))

        node = res.register(self.bin_op(self.arith_expr, (TT_EE, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE)))
        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                "Expected int, float, '+', '-' or '(', 'NOT"
            ))

        return res.success(node)

    # Handle overall expression parsing - create respective Nodes based on token type
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

            # after an identifier an expression is accepted
            expr = res.register(self.expr())
            if res.error:
                return res

            return res.success(VarAssignNode(var_name, expr))

        # variable access
        elif self.current_token.matches(TT_KEYWORD, 'SHOW'):
            res.register_advancement()
            self.advance()

            # once the keyword is advanced only an identifier is accepted
            if self.current_token.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_token.pos_start, self.current_token.pos_end,
                    'Expected identifier'
                ))

            return res.success(VarAccessNode(self.current_token))

        node = res.register(self.bin_op(self.comp_expr, ((TT_KEYWORD, 'AND'), (TT_KEYWORD, 'OR'))))

        # invalid input
        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end,
                'Expected Keyword, \'+\', \'-\' or \'(\', \'NOT\''
            ))

        return res.success(node)

    # ops - operators | func - term/factor based on the grammar that's defined
    def bin_op(self, func_a, ops, func_b=None):
        if func_b is None:
            func_b = func_a

        res = ParseResult()
        left = res.register(func_a())
        if res.error:
            return res
        while self.current_token.type in ops or (self.current_token.type, self.current_token.value) in ops:
            op_tok = self.current_token
            res.register_advancement()
            self.advance()
            right = res.register(func_b())
            if res.error:
                return res
            left = BinOpNode(left, op_tok, right)
        return res.success(left)
