"""Runtime result tracking for the SimpleScript interpreter.

This module provides the RTResult class used to track the success
or failure of runtime operations during interpretation.
"""

from typing import Any


class RTResult:
    """Tracks the result of a runtime operation.

    Accumulates the computed value or error state as the interpreter
    evaluates AST nodes.

    Attributes:
        value: The computed value, if the operation was successful.
        error (Optional[Error]): The error encountered, if any.
    """

    def __init__(self) -> None:
        self.value: Any = None
        self.error = None

    def register(self, res: "RTResult") -> Any:
        """Register the result of a sub-operation.

        Absorbs any error from the sub-result and returns the computed value.

        Args:
            res: The RTResult from a sub-operation.

        Returns:
            The value from the sub-result.
        """
        if res.error:
            self.error = res.error
        return res.value

    def success(self, value: Any) -> "RTResult":
        """Mark this result as successful.

        Args:
            value: The successfully computed value.

        Returns:
            This RTResult instance for method chaining.
        """
        self.value = value
        return self

    def failure(self, error) -> "RTResult":
        """Mark this result as failed.

        Args:
            error: The error that caused the failure.

        Returns:
            This RTResult instance for method chaining.
        """
        self.error = error
        return self
