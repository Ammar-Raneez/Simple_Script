"""Error location visualization utility.

This module provides a function to generate a visual representation
of error locations in source code using arrow (^) characters.
"""

from simplescript.tokens.position import Position


def string_with_arrows(text: str, pos_start: Position, pos_end: Position) -> str:
    """Generate a string highlighting an error location with arrows.

    Creates a visual representation of source code with '^' characters
    underneath the region between pos_start and pos_end, making it easy
    to identify where an error occurred.

    Args:
        text: The full source text.
        pos_start: Starting position of the error region.
        pos_end: Ending position of the error region.

    Returns:
        A string containing the relevant source lines with '^' arrows
        pointing to the error location.

    Example:
        >>> print(string_with_arrows("VAR A =", pos_start, pos_end))
        VAR A =
              ^
    """
    result = ''

    # Calculate indices
    idx_start = max(text.rfind('\n', 0, pos_start.index), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0:
        idx_end = len(text)

    # Generate each line
    line_count = pos_end.lnNumber - pos_start.lnNumber + 1
    for i in range(line_count):
        # Calculate line columns
        line = text[idx_start:idx_end]
        col_start = pos_start.colNumber if i == 0 else 0
        col_end = pos_end.colNumber if i == line_count - 1 else len(line) - 1

        # Append to result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Re-calculate indices
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0:
            idx_end = len(text)

    return result.replace('\t', '')
