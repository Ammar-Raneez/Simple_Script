"""Symbol table for variable and function storage.

This module provides the SymbolTable class used to store and retrieve
variable and function bindings during SimpleScript execution.
"""

from typing import Any, Optional


class SymbolTable:
    """Stores variable and function bindings for a given scope.

    Supports nested scoping through a parent reference, allowing inner
    scopes (such as function bodies) to access variables from outer scopes.

    Args:
        parent: The parent symbol table for outer scope lookups.

    Attributes:
        parent (Optional[SymbolTable]): Parent table for scope chaining.
        symbols (dict): Dictionary mapping names to their values.
    """

    def __init__(self, parent: Optional['SymbolTable'] = None) -> None:
        self.parent = parent
        self.symbols: dict[str, Any] = {}

    def get(self, name: str) -> Optional[Any]:
        """Retrieve a value by name from this scope.

        Args:
            name: The variable or function name to look up.

        Returns:
            The value associated with the name, or None if not found.
        """
        value = self.symbols.get(name, None)
        return value

    def set(self, name: str, value: Any) -> None:
        """Set a variable or function binding in this scope.

        Args:
            name: The variable or function name.
            value: The value to associate with the name.
        """
        self.symbols[name] = value

    def remove(self, name: str) -> None:
        """Remove a variable or function binding from this scope.

        Args:
            name: The variable or function name to remove.

        Raises:
            KeyError: If the name does not exist in this scope.
        """
        del self.symbols[name]
