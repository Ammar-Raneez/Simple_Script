from lexer import *
from parse import *


def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()
    print(tokens)
    # Generate AST (abstract syntax tree)
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    return ast.node, None
