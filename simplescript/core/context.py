"""Execution context for the SimpleScript interpreter.

This module provides the Context class, which is used to track runtime
execution state including variable scope and call stack information
for error traceback generation.
"""

from typing import Optional
from simplescript.tokens.position import Position


class Context:
    """Represents an execution context in the SimpleScript runtime.

    Contexts form a chain that tracks the call stack during execution.
    Each context has its own symbol table for variable scoping and
    references to its parent context for traceback generation.

    Args:
        display_name: Human-readable name for this context (e.g., function name).
        parent: The parent context that created this one.
        parent_entry_pos: The source position where this context was entered.

    Attributes:
        display_name (str): Name of this context for display in tracebacks.
        parent (Optional[Context]): Parent context in the call chain.
        parent_entry_pos (Optional[Position]): Position where parent entered this context.
        symbol_table (Optional[SymbolTable]): Variable symbol table for this scope.
    """

    def __init__(self, display_name: str,
                 parent: Optional['Context'] = None,
                 parent_entry_pos: Optional[Position] = None) -> None:
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
