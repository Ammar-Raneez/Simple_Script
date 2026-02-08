"""Parse result tracking for the SimpleScript parser.

This module provides the ParseResult class used to track the success
or failure of parsing operations, along with how many tokens were consumed.
"""


class ParseResult:
    """Tracks the result of a parsing operation.

    Accumulates the parsed AST node or error state as the parser processes
    tokens. Tracks how many tokens have been consumed to support error
    recovery decisions.

    Attributes:
        error (Optional[Error]): The error encountered during parsing, if any.
        node: The AST node produced by parsing, if successful.
        advance_count (int): Number of tokens consumed during parsing.
    """

    def __init__(self) -> None:
        self.error = None
        self.node = None
        self.advance_count: int = 0

    def register_advancement(self) -> None:
        """Record that a token has been consumed."""
        self.advance_count += 1

    def register(self, res: 'ParseResult'):
        """Register the result of a sub-parse operation.

        Absorbs the advance count and any error from the sub-result,
        and returns the parsed node.

        Args:
            res: The ParseResult from a sub-parse operation.

        Returns:
            The AST node from the sub-result.
        """
        self.advance_count += res.advance_count
        if res.error:
            self.error = res.error
        return res.node

    def success(self, node) -> 'ParseResult':
        """Mark this parse result as successful.

        Args:
            node: The AST node that was successfully parsed.

        Returns:
            This ParseResult instance for method chaining.
        """
        self.node = node
        return self

    def failure(self, error) -> 'ParseResult':
        """Mark this parse result as failed.

        Only overwrites the existing error if no tokens have been consumed
        yet (advance_count == 0), which allows the most specific error
        to be preserved.

        Args:
            error: The error that caused the parse failure.

        Returns:
            This ParseResult instance for method chaining.
        """
        if not self.error or self.advance_count == 0:
            self.error = error
        return self
