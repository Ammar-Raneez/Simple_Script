"""Main runtime entry point for the SimpleScript interpreter.

This module provides the ``run`` function that ties together the lexer,
parser, and interpreter to execute SimpleScript source code.
"""

from typing import Tuple, Optional, Any
from simplescript.core.lexer import Lexer
from simplescript.core.parser import Parser
from simplescript.core.interpreter import Interpreter
from simplescript.core.context import Context
from simplescript.utils.symbol_table import SymbolTable
from simplescript.errors.errors import Error

# Global symbol table persists across multiple run() calls (REPL sessions)
global_symbol_table = SymbolTable()


def run(file_name: str, text: str) -> Tuple[Optional[Any], Optional[Error]]:
    """Execute SimpleScript source code and return the result.

    Performs the full interpretation pipeline: lexing, parsing, and
    interpreting. The global symbol table is shared across calls,
    allowing variables defined in one call to be accessed in subsequent
    calls (useful for REPL sessions).

    Args:
        file_name: The name of the source file (used for error reporting).
        text: The SimpleScript source code to execute.

    Returns:
        A tuple of (result, error):
            - On success: (value, None) where value is the computed result.
            - On failure: (None, error) where error describes what went wrong.

    Example:
        >>> result, error = run('<stdin>', 'VAR x = 10 + 5')
        >>> print(result)
        15
    """
    # Tokenize
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Parse into AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Interpret
    interpreter = Interpreter()
    context = Context('<simplescript>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
