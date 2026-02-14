from typing import Optional, Tuple
from simplescript.errors.errors import RTError
from simplescript.types.base import Value
from simplescript.types.number import Number


class List(Value):
    """Represents a list of values in SimpleScript.

    Supports appending elements, removing elements by index, extending lists,
    and retrieving elements by index.

    Args:
        elements: List of values to initialize the list with.

    Attributes:
        elements: List of values.
    """

    def __init__(self, elements: list) -> None:
        super().__init__()
        self.elements = elements

    def added_to(self, other: Value) -> Tuple[Optional["List"], Optional[RTError]]:
        """Append another value to this list.

        Args:
            other: The value to append.

        Returns:
            A tuple of (result List, None) on success, or (None, error).
        """
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subbed_by(self, other: Value) -> Tuple[Optional["List"], Optional[RTError]]:
        """Remove an element from this list by index.

        Args:
            other: The index of the element to remove.

        Returns:
            A tuple of (result List, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RTError(
                    other.pos_start,
                    other.pos_end,
                    "Element at this index could not be removed from list because index is out of bounds",
                    self.context,
                )
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other: Value) -> Tuple[Optional["List"], Optional[RTError]]:
        """Extend this list with another list.

        Args:
            other: The list to extend this list with.

        Returns:
            A tuple of (result List, None) on success, or (None, error).
        """
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other: Value) -> Tuple[Optional["List"], Optional[RTError]]:
        """Retrieve an element from this list by index.

        Args:
            other: The index of the element to retrieve.

        Returns:
            A tuple of (result List, None) on success, or (None, error).
        """
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RTError(
                    other.pos_start,
                    other.pos_end,
                    "Element at this index could not be retrieved from list because index is out of bounds",
                    self.context,
                )
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        """Create a copy of this list.

        Returns:
            A new List instance with the same elements, position, and context.
        """
        copy = List(self.elements[:])
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self) -> str:
        """Return a string representation of this list."""
        return f'[{", ".join([str(x) for x in self.elements])}]'
