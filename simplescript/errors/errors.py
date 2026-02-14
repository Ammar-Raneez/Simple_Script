"""Error classes for the SimpleScript interpreter.

This module defines the error hierarchy used throughout SimpleScript,
from lexer errors (illegal characters) through parser errors (invalid syntax)
to runtime errors (division by zero, undefined variables, etc.).
"""

from simplescript.core.context import Context
from simplescript.tokens.position import Position
from simplescript.utils.string_with_arrows import string_with_arrows


class Error:
    """Base error class for all SimpleScript errors.

    Provides common error formatting including the error name, details,
    file location, and a visual pointer to the error in the source code.

    Args:
        pos_start: Starting position of the error in source code.
        pos_end: Ending position of the error in source code.
        error_name: Name/category of the error.
        details: Detailed description of what went wrong.

    Attributes:
        pos_start (Position): Starting position of the error.
        pos_end (Position): Ending position of the error.
        error_name (str): Name/category of the error.
        details (str): Detailed description of the error.
    """

    def __init__(
        self, pos_start: Position, pos_end: Position, error_name: str, details: str
    ) -> None:
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self) -> str:
        """Format the error as a human-readable string.

        Returns:
            A formatted error message including the error name, details,
            file location, and a visual pointer to the error.
        """
        result = f"{self.error_name}: {self.details}\n"
        result += f"File {self.pos_start.fName}, line {self.pos_start.lnNumber + 1}"
        result += "\n\n" + string_with_arrows(
            self.pos_start.fText, self.pos_start, self.pos_end
        )
        return result


class IllegalCharError(Error):
    """Error raised when an illegal character is encountered during lexing.

    Args:
        pos_start: Starting position of the illegal character.
        pos_end: Ending position of the illegal character.
        details: Description of the illegal character.
    """

    def __init__(self, pos_start: Position, pos_end: Position, details: str) -> None:
        super().__init__(pos_start, pos_end, "Illegal Character", details)


class ExpectedCharError(Error):
    """Error raised when an expected character is missing during lexing.

    Args:
        pos_start: Starting position where the character was expected.
        pos_end: Ending position of the error region.
        details: Description of the expected character.
    """

    def __init__(self, pos_start: Position, pos_end: Position, details: str) -> None:
        super().__init__(pos_start, pos_end, "Expected Character", details)


class InvalidSyntaxError(Error):
    """Error raised when invalid syntax is encountered during parsing.

    Args:
        pos_start: Starting position of the syntax error.
        pos_end: Ending position of the syntax error.
        details: Description of the syntax error.
    """

    def __init__(
        self, pos_start: Position, pos_end: Position, details: str = ""
    ) -> None:
        super().__init__(pos_start, pos_end, "Invalid Syntax", details)


class RTError(Error):
    """Error raised during runtime execution.

    Extends the base Error class with traceback generation capability,
    showing the chain of contexts (function calls) that led to the error.

    Args:
        pos_start: Starting position of the runtime error.
        pos_end: Ending position of the runtime error.
        details: Description of the runtime error.
        context: The execution context where the error occurred.

    Attributes:
        context (Context): The execution context for traceback generation.
    """

    def __init__(
        self, pos_start: Position, pos_end: Position, details: str, context: Context
    ) -> None:
        super().__init__(pos_start, pos_end, "Runtime Error", details)
        self.context = context

    def as_string(self) -> str:
        """Format the runtime error with a full traceback.

        Returns:
            A formatted error message including the traceback, error name,
            details, and a visual pointer to the error location.
        """
        result = self.generate_traceback()
        result += f"{self.error_name}: {self.details}"
        result += "\n\n" + string_with_arrows(
            self.pos_start.fText, self.pos_start, self.pos_end
        )
        return result

    def generate_traceback(self) -> str:
        """Generate a traceback showing the chain of execution contexts.

        Walks up the context chain from the error location to the top-level
        context, producing a traceback similar to Python's format.

        Returns:
            A formatted traceback string.
        """
        result = ""
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result = (
                f"  File {pos.fName}, line {str(pos.lnNumber + 1)}, "
                f"in {ctx.display_name}\n"
            ) + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return "Traceback (most recent call last):\n" + result
