"""Constants and token type definitions for SimpleScript.

This module defines all token type identifiers, keywords, and character
sets used throughout the SimpleScript interpreter.
"""

import string as _string

# Character sets
DIGITS: str = "0123456789"
"""Valid digit characters for number parsing."""

LETTERS: str = _string.ascii_letters
"""Valid letter characters for identifier parsing (A-Z, a-z)."""

# Token type identifiers
TT_INT: str = "INT"
"""Integer literal token."""

TT_FLOAT: str = "FLOAT"
"""Float literal token."""

TT_STRING: str = "STRING"
"""String literal token."""

TT_PLUS: str = "PLUS"
"""Addition operator (+) token."""

TT_MINUS: str = "MINUS"
"""Subtraction operator (-) token."""

TT_MUL: str = "MUL"
"""Multiplication operator (*) token."""

TT_DIV: str = "DIV"
"""Division operator (/) token."""

TT_POW: str = "POW"
"""Power operator (^) token."""

TT_LPAREN: str = "LPAREN"
"""Left parenthesis token."""

TT_RPAREN: str = "RPAREN"
"""Right parenthesis token."""

TT_EE: str = "EE"
"""Equality comparison (==) token."""

TT_EQ: str = "EQ"
"""Assignment (=) token."""

TT_NE: str = "NE"
"""Not equal (!=) token."""

TT_LT: str = "LT"
"""Less than (<) token."""

TT_GT: str = "GT"
"""Greater than (>) token."""

TT_LTE: str = "LTE"
"""Less than or equal (<=) token."""

TT_GTE: str = "GTE"
"""Greater than or equal (>=) token."""

TT_EOF: str = "EOF"
"""End of file token."""

TT_IDENTIFIER: str = "IDENTIFIER"
"""Identifier (variable/function name) token."""

TT_KEYWORD: str = "KEYWORD"
"""Language keyword token."""

TT_COMMA: str = "COMMA"
"""Comma separator token."""

TT_ARROW: str = "ARROW"
"""Arrow (->) token for function definitions."""

TT_LSQUARE: str = "LSQUARE"
"""Left square bracket token for arrays."""

TT_RSQUARE: str = "RSQUARE"
"""Right square bracket token for arrays."""

TT_LBRACE: str = "LBRACE"
"""Left curly brace token for maps."""

TT_RBRACE: str = "RBRACE"
"""Right curly brace token for maps."""

TT_COLON: str = "COLON"
"""Colon token for map key-value pairs."""

KEYWORDS: list[str] = [
    "SHOW",
    "VAR",
    "AND",
    "OR",
    "NOT",
    "IF",
    "THEN",
    "ELIF",
    "ELSE",
    "FOR",
    "TO",
    "STEP",
    "WHILE",
    "FUNC",
]
"""List of reserved keywords in SimpleScript."""
