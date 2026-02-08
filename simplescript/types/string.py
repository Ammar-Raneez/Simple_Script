"""String type for the SimpleScript runtime.

This module defines the String class (internally String), which represents
string values and supports concatenation and repetition operations.
"""

from typing import Tuple, Optional
from simplescript.types.base import Value


class String(Value):
    """Represents a string value in SimpleScript.

    Supports concatenation with other strings (using +) and repetition
    with numbers (using *).

    Args:
        value: The string content.

    Attributes:
        value (str): The string content.
    """

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def added_to(self, other: Value) -> Tuple[Optional['String'], Optional[Exception]]:
        """Concatenate another string to this one.

        Args:
            other: The string value to concatenate.

        Returns:
            A tuple of (result String, None) on success, or (None, error)
            if the other value is not a string.
        """
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other: Value) -> Tuple[Optional['String'], Optional[Exception]]:
        """Repeat this string a given number of times.

        Args:
            other: A Number value specifying the repetition count.

        Returns:
            A tuple of (result String, None) on success, or (None, error)
            if the other value is not a number.
        """
        from simplescript.types.number import Number
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def is_true(self) -> bool:
        """Check if this string is truthy (non-empty).

        Returns:
            True if the string has length greater than zero.
        """
        return len(self.value) > 0

    def copy(self) -> 'String':
        """Create a copy of this String.

        Returns:
            A new String instance with the same value, position, and context.
        """
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self) -> str:
        return f'"{self.value}"'
