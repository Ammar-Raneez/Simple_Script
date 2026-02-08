"""SimpleScript - A simple programming language interpreter.

SimpleScript is a basic command language that supports variables,
conditional statements, loops, functions, and string operations.

Example:
    >>> import simplescript
    >>> result, error = simplescript.run('<stdin>', 'VAR x = 10 + 5')
    >>> print(result)
    15
"""

from simplescript.__version__ import __version__, __author__, __license__
from simplescript.runtime import run

__all__ = ['run', '__version__', '__author__', '__license__']
