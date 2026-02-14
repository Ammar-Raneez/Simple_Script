"""Function type for the SimpleScript runtime.

This module defines the Function class, which represents user-defined
functions that can be called with arguments during execution.
"""

from typing import List, Optional
from simplescript.types.base import Value
from simplescript.utils.rt_result import RTResult
from simplescript.core.context import Context
from simplescript.utils.symbol_table import SymbolTable
from simplescript.errors.errors import RTError


class Function(Value):
    """Represents a user-defined function in SimpleScript.

    Functions have a name (or are anonymous), a body expression, and a
    list of parameter names. When executed, they create a new scope and
    evaluate their body expression.

    Args:
        name: The function name, or None for anonymous functions.
        body_node: The AST node for the function body expression.
        arg_names: List of parameter name strings.

    Attributes:
        name (str): The function name (defaults to '<anonymous>').
        body_node: The body expression AST node.
        arg_names (list[str]): Parameter name strings.
    """

    def __init__(self, name: Optional[str], body_node,
                 arg_names: List[str]) -> None:
        super().__init__()
        self.name = name or "<anonymous>"
        self.body_node = body_node
        self.arg_names = arg_names

    def execute(self, args: list) -> RTResult:
        """Execute this function with the given arguments.

        Creates a new execution context with its own symbol table,
        binds the arguments to parameter names, and evaluates the
        function body.

        Args:
            args: List of argument values to pass to the function.

        Returns:
            An RTResult containing the return value or an error if
            the wrong number of arguments was provided or if the
            body evaluation fails.
        """
        # Import here to avoid circular import
        from simplescript.core.interpreter import Interpreter

        res = RTResult()
        interpreter = Interpreter()
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)

        if len(args) > len(self.arg_names):
            return res.failure(
                RTError(
                    self.pos_start,
                    self.pos_end,
                    f"{len(args) - len(self.arg_names)} too many args passed into '{self.name}'",
                    self.context,
                )
            )

        if len(args) < len(self.arg_names):
            return res.failure(
                RTError(
                    self.pos_start,
                    self.pos_end,
                    f"{len(self.arg_names) - len(args)} too few args passed into '{self.name}'",
                    self.context,
                )
            )

        for i in range(len(args)):
            arg_name = self.arg_names[i]
            arg_value = args[i]
            arg_value.set_context(new_context)
            new_context.symbol_table.set(arg_name, arg_value)

        value = res.register(interpreter.visit(self.body_node, new_context))
        if res.error:
            return res
        return res.success(value)

    def copy(self) -> 'Function':
        """Create a copy of this Function.

        Returns:
            A new Function instance with the same name, body, arguments,
            position, and context.
        """
        copy = Function(self.name, self.body_node, self.arg_names)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self) -> str:
        """Return a string representation of this function."""
        return f"<function {self.name}>"
