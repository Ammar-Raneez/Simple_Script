from typing import Optional, Tuple
from simplescript.errors.errors import RTError
from simplescript.types.base import Value
from simplescript.types.string import String


class Map(Value):
    """Represents a map (dictionary) of key-value pairs in SimpleScript.

    Supports getting values by key, adding/updating key-value pairs,
    removing keys, and merging with other maps.

    Args:
        elements: Dictionary of key-value pairs.

    Attributes:
        elements: Dictionary mapping keys to values.
    """

    def __init__(self, elements: dict) -> None:
        super().__init__()
        self.elements = elements

    def added_to(self, other: Value) -> Tuple[Optional["Map"], Optional[RTError]]:
        """Add or update a key-value pair in this map.

        Args:
            other: A Map containing the key-value pair(s) to add/update.

        Returns:
            A tuple of (result Map, None) on success, or (None, error).
        """
        if isinstance(other, Map):
            new_map = self.copy()
            new_map.elements.update(other.elements)
            return new_map, None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other: Value) -> Tuple[Optional["Map"], Optional[RTError]]:
        """Remove a key from this map.

        Args:
            other: The key to remove (String).

        Returns:
            A tuple of (result Map, None) on success, or (None, error).
        """
        if isinstance(other, String):
            new_map = self.copy()
            try:
                del new_map.elements[other.value]
                return new_map, None
            except KeyError:
                return None, RTError(
                    other.pos_start,
                    other.pos_end,
                    f"Key '{other.value}' does not exist in map",
                    self.context,
                )
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other: Value) -> Tuple[Optional["Map"], Optional[RTError]]:
        """Merge this map with another map.

        Args:
            other: The map to merge with this map.

        Returns:
            A tuple of (result Map, None) on success, or (None, error).
        """
        if isinstance(other, Map):
            new_map = self.copy()
            new_map.elements.update(other.elements)
            return new_map, None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other: Value) -> Tuple[Optional[Value], Optional[RTError]]:
        """Retrieve a value from this map by key.

        Args:
            other: The key to retrieve (String).

        Returns:
            A tuple of (value, None) on success, or (None, error).
        """
        if isinstance(other, String):
            try:
                return self.elements[other.value], None
            except KeyError:
                return None, RTError(
                    other.pos_start,
                    other.pos_end,
                    f"Key '{other.value}' does not exist in map",
                    self.context,
                )
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        """Create a copy of this map.

        Returns:
            A new Map instance with the same elements, position, and context.
        """
        copy = Map(self.elements.copy())
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self) -> str:
        """Return a string representation of this map."""
        items = [f'"{k}": {v}' for k, v in self.elements.items()]
        return "{" + ", ".join(items) + "}"
