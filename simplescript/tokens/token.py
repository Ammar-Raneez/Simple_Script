"""Token representation for the SimpleScript lexer.

This module provides the Token class, which represents a single lexical
token produced by the lexer during tokenization.
"""

from typing import Any, Optional
from simplescript.tokens.position import Position


class Token:
    """Represents a single lexical token.

    A token holds the type of the lexical element (e.g., INT, PLUS, KEYWORD)
    along with an optional value (e.g., the actual number or identifier string),
    and its position within the source text.

    Args:
        type_: The token type identifier (from constants).
        value: The actual value of the token, if applicable.
        pos_start: Starting position of the token in source text.
        pos_end: Ending position of the token in source text.

    Attributes:
        type (str): The token type identifier.
        value: The actual value of the token.
        pos_start (Position): Starting position in source text.
        pos_end (Position): Ending position in source text.
    """

    def __init__(
        self,
        type_: str,
        value: Any = None,
        pos_start: Optional[Position] = None,
        pos_end: Optional[Position] = None,
    ) -> None:
        self.type = type_
        self.value = value
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        if pos_end:
            self.pos_end = pos_end

    def matches(self, type_: str, value: Any) -> bool:
        """Check if this token matches a given type and value.

        Args:
            type_: The token type to match against.
            value: The token value to match against.

        Returns:
            True if both type and value match, False otherwise.
        """
        return self.type == type_ and self.value == value

    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}: {self.value}"
        return f"{self.type}"
