"""Number type for the SimpleScript runtime.

This module defines the Number class, which represents integer and
floating-point values and supports arithmetic, comparison, and logical
operations.
"""

from typing import Tuple, Optional, Union
from simplescript.types.base import Value
from simplescript.errors.errors import RTError


class Number(Value):
    """Represents a numeric value (integer or float) in SimpleScript.

    Supports all arithmetic operations (addition, subtraction, multiplication,
    division, exponentiation), comparison operations, and logical operations.

    Args:
        value: The numeric value (int or float).

    Attributes:
        value (Union[int, float]): The numeric value.
    """

    def __init__(self, value: Union[int, float]) -> None:
        super().__init__()
        self.value = value

    def added_to(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Add another number to this one.

        Args:
            other: The value to add.

        Returns:
            A tuple of (result Number, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        return None, self.illegal_operation(other)

    def subbed_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Subtract another number from this one.

        Args:
            other: The value to subtract.

        Returns:
            A tuple of (result Number, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        return None, self.illegal_operation(other)

    def multed_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Multiply this number by another.

        Args:
            other: The value to multiply by.

        Returns:
            A tuple of (result Number, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        return None, self.illegal_operation(other)

    def dived_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Divide this number by another.

        Args:
            other: The divisor value.

        Returns:
            A tuple of (result Number, None) on success, or (None, RTError)
            if dividing by zero or incompatible type.
        """
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context), None
        return None, self.illegal_operation(other)

    def powed_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Raise this number to the power of another.

        Args:
            other: The exponent value.

        Returns:
            A tuple of (result Number, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check equality with another number.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if equal, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check inequality with another number.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if not equal, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check if this number is less than another.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if less than, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check if this number is greater than another.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if greater than, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check if this number is less than or equal to another.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if less than or equal, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Check if this number is greater than or equal to another.

        Args:
            other: The value to compare against.

        Returns:
            Number(1) if greater than or equal, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def anded_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Perform logical AND with another number.

        Args:
            other: The right-hand operand.

        Returns:
            Number(1) if both are truthy, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def ored_by(self, other: Value) -> Tuple[Optional['Number'], Optional[RTError]]:
        """Perform logical OR with another number.

        Args:
            other: The right-hand operand.

        Returns:
            Number(1) if either is truthy, Number(0) otherwise.
        """
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
        return None, self.illegal_operation(other)

    def notted(self) -> Tuple['Number', None]:
        """Perform logical NOT on this number.

        Returns:
            Number(1) if this value is 0, Number(0) otherwise.
        """
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    def is_true(self) -> bool:
        """Check if this number is truthy (non-zero).

        Returns:
            True if the value is not zero.
        """
        return self.value != 0

    def copy(self) -> 'Number':
        """Create a copy of this Number.

        Returns:
            A new Number instance with the same value, position, and context.
        """
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self) -> str:
        return str(self.value)
