"""Runtime value types for the SimpleScript interpreter."""

from simplescript.types.base import Value
from simplescript.types.number import Number
from simplescript.types.string import String
from simplescript.types.function import Function

__all__ = ["Value", "Number", "String", "Function"]
