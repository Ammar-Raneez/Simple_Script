"""Position tracking for the SimpleScript lexer.

This module provides the Position class used to track the current location
within source code during lexical analysis and error reporting.
"""

from typing import Optional


class Position:
    """Tracks a position within source code text.

    Maintains the current index, line number, and column number within
    the source text. Used throughout the lexer, parser, and error reporting
    to pinpoint exact locations in the source code.

    Args:
        index: Character index in the source text.
        ln_number: Current line number (0-based).
        col_number: Current column number (0-based).
        f_name: Name of the source file.
        f_text: Full source text content.

    Attributes:
        index (int): Character index in the source text.
        lnNumber (int): Current line number (0-based).
        colNumber (int): Current column number (0-based).
        fName (str): Name of the source file.
        fText (str): Full source text content.
    """

    def __init__(
        self, index: int, ln_number: int, col_number: int, f_name: str, f_text: str
    ) -> None:
        self.index = index
        self.lnNumber = ln_number
        self.colNumber = col_number
        self.fName = f_name
        self.fText = f_text

    def advance(self, current_char: Optional[str] = None) -> "Position":
        """Advance the position by one character.

        Increments the index and column number. If the current character
        is a newline, the line number is incremented and the column number
        is reset to zero.

        Args:
            current_char: The character at the current position before advancing.

        Returns:
            This Position instance for method chaining.
        """
        self.index += 1
        self.colNumber += 1

        if current_char == "\n":
            self.lnNumber += 1
            self.colNumber = 0
        return self

    def copy(self) -> "Position":
        """Create a copy of this position.

        Returns:
            A new Position instance with the same values.
        """
        return Position(
            self.index, self.lnNumber, self.colNumber, self.fName, self.fText
        )
