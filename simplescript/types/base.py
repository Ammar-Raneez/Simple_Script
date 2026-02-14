"""Base value type for the SimpleScript type system.

This module defines the Value base class from which all SimpleScript
runtime types (Number, String, Function) inherit. It provides default
implementations for all operations that can be overridden by subclasses.
"""

from typing import Optional, Tuple
from simplescript.errors.errors import RTError
from simplescript.utils.rt_result import RTResult


class Value:
    """Base class for all runtime value types in SimpleScript.

    Provides default implementations for arithmetic, comparison, and
    logical operations that return an 'Illegal operation' error. Subclasses
    override the operations they support.

    Attributes:
        pos_start (Optional[Position]): Start position in source text.
        pos_end (Optional[Position]): End position in source text.
        context (Optional[Context]): The execution context.
    """

    def __init__(self) -> None:
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None) -> 'Value':
        """Set the source position of this value.

        Args:
            pos_start: Starting position in source text.
            pos_end: Ending position in source text.

        Returns:
            This Value instance for method chaining.
        """
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None) -> 'Value':
        """Set the execution context of this value.

        Args:
            context: The execution context.

        Returns:
            This Value instance for method chaining.
        """
        self.context = context
        return self

    def added_to(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform addition with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def subbed_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform subtraction with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def multed_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform multiplication with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def dived_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform division with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def powed_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform exponentiation with another value.

        Args:
            other: The right-hand operand (exponent).

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform equality comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform not-equal comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform less-than comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform greater-than comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform less-than-or-equal comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform greater-than-or-equal comparison.

        Args:
            other: The value to compare against.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def anded_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform logical AND with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def ored_by(self, other: 'Value') -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform logical OR with another value.

        Args:
            other: The right-hand operand.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def notted(self, other: 'Value' = None) -> Tuple[Optional['Value'], Optional[RTError]]:
        """Perform logical NOT.

        Args:
            other: Unused, kept for interface consistency.

        Returns:
            A tuple of (result, error). Default returns an illegal operation error.
        """
        return None, self.illegal_operation(other)

    def execute(self, args: list) -> RTResult:
        """Execute this value as a callable (for functions).

        Args:
            args: List of argument values.

        Returns:
            An RTResult with an illegal operation error by default.
        """
        return RTResult().failure(self.illegal_operation())

    def copy(self) -> 'Value':
        """Create a copy of this value.

        Returns:
            A new Value instance with the same state.

        Raises:
            Exception: If the subclass does not implement copy.
        """
        raise Exception('No copy method defined')

    def is_true(self) -> bool:
        """Check if this value is truthy.

        Returns:
            False by default. Subclasses override for their truthiness logic.
        """
        return False

    def illegal_operation(self, other: Optional['Value'] = None) -> RTError:
        """Create an illegal operation error.

        Args:
            other: The other operand involved in the operation, if any.

        Returns:
            An RTError describing the illegal operation.
        """
        if not other:
            other = self

        return RTError(
            self.pos_start, other.pos_end,
            'Illegal operation',
            self.context
        )
