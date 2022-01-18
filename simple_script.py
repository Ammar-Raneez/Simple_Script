from lexer import *
from parse import *
from interpreter import *
from context import *
from symbol_table import *

# Create a global symbol table to keep track of variable names and their values
global_symbol_table = SymbolTable()


def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()
    # return tokens, error
    if error:
        return None, error

    # Generate AST (abstract syntax tree)
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    return ast.node, None
    # # Run program
    # interpreter = Interpreter()
    # context = Context('<simplescript>')
    # context.symbol_table = global_symbol_table
    # result = interpreter.visit(ast.node, context)
    #
    # return result.value, result.error
