"""Interpreter (tree-walker) for the SimpleScript language.

This module provides the Interpreter class that evaluates an Abstract
Syntax Tree (AST) produced by the parser, producing runtime values.
"""

from simplescript.types.list import List
from simplescript.utils.rt_result import RTResult
from simplescript.core.constants import (
    TT_PLUS, TT_MINUS, TT_MUL, TT_DIV, TT_POW,
    TT_EE, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE,
    TT_KEYWORD,
)
from simplescript.types.number import Number
from simplescript.types.function import Function
from simplescript.types.string import String
from simplescript.errors.errors import RTError
from simplescript.core.context import Context


class Interpreter:
    """Evaluates an AST by walking the tree and computing runtime values.

    Uses the visitor pattern: for each AST node type ``XxxNode``, a method
    ``visit_XxxNode`` is called. Each visitor method returns an RTResult
    containing the computed value or an error.

    Example:
        >>> interpreter = Interpreter()
        >>> context = Context('<program>')
        >>> result = interpreter.visit(ast_root, context)
    """

    def visit(self, node, context: Context) -> RTResult:
        """Dispatch to the appropriate visitor method for the given node.

        Args:
            node: The AST node to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the computed value or an error.

        Raises:
            Exception: If no visitor method is defined for the node type.
        """
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context: Context) -> None:
        """Handle AST node types with no defined visitor.

        Args:
            node: The unhandled AST node.
            context: The current execution context.

        Raises:
            Exception: Always, indicating the missing visitor method.
        """
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node, context: Context) -> RTResult:
        """Evaluate a numeric literal node.

        Args:
            node: The NumberNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the Number value.
        """
        return RTResult().success(
            Number(node.tok.value).set_context(context).set_pos(
                node.pos_start, node.pos_end
            )
        )

    def visit_StringNode(self, node, context: Context) -> RTResult:
        """Evaluate a string literal node.

        Args:
            node: The StringNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the String value.
        """
        return RTResult().success(
            String(node.tok.value).set_context(context).set_pos(
                node.pos_start, node.pos_end
            )
        )

    def visit_VarAccessNode(self, node, context: Context) -> RTResult:
        """Evaluate a variable access expression.

        Args:
            node: The VarAccessNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the variable's value, or an error
            if the variable is not defined.
        """
        res = RTResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        value = value.copy().set_pos(node.pos_start, node.pos_end)
        return res.success(value)

    def visit_VarAssignNode(self, node, context: Context) -> RTResult:
        """Evaluate a variable assignment statement.

        Args:
            node: The VarAssignNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the assigned value, or an error
            if the value expression fails.
        """
        res = RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.error:
            return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context: Context) -> RTResult:
        """Evaluate a binary operation expression.

        Handles arithmetic (+, -, ``*``, /, ^), comparison (==, !=, <, >, <=, >=),
        and logical (AND, OR) operations.

        Args:
            node: The BinOpNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the operation result, or an error.
        """
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error:
            return res
        right = res.register(self.visit(node.right_node, context))
        if res.error:
            return res

        result, error = None, None
        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == TT_MUL:
            result, error = left.multed_by(right)
        elif node.op_tok.type == TT_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.type == TT_POW:
            result, error = left.powed_by(right)
        elif node.op_tok.type == TT_EE:
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == TT_NE:
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == TT_LT:
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == TT_GT:
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == TT_LTE:
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == TT_GTE:
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.matches(TT_KEYWORD, 'AND'):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'OR'):
            result, error = left.ored_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context: Context) -> RTResult:
        """Evaluate a unary operation expression (negation, NOT).

        Args:
            node: The UnaryOpNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the operation result, or an error.
        """
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error:
            return res

        error = None
        if node.op_tok.type == TT_MINUS:
            number, error = number.multed_by(Number(-1))
        elif node.op_tok.type.matches(TT_KEYWORD, 'NOT'):
            number, error = number.notted()

        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))

    def visit_IfNode(self, node, context: Context) -> RTResult:
        """Evaluate an if/elif/else conditional expression.

        Args:
            node: The IfNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the value of the matched branch,
            or None if no branch matches and there is no else clause.
        """
        res = RTResult()

        for condition, expr in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.error:
                return res

            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.error:
                    return res
                return res.success(expr_value)

        if node.else_case:
            else_value = res.register(self.visit(node.else_case, context))
            if res.error:
                return res
            return res.success(else_value)

        return res.success(None)

    def visit_ForNode(self, node, context: Context) -> RTResult:
        """Evaluate a for loop expression.

        Args:
            node: The ForNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the List value on completion, or an error.
        """
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value_node, context))
        if res.error:
            return res

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.error:
            return res

        if node.step_value_node:
            step_value = res.register(self.visit(node.step_value_node, context))
            if res.error:
                return res
        else:
            step_value = Number(1)

        i = start_value.value

        if step_value.value >= 0:
            def condition():
                return i < end_value.value
        else:
            def condition():
                return i > end_value.value

        while condition():
            context.symbol_table.set(node.var_name_tok.value, Number(i))
            i += step_value.value

            elements.append(res.register(self.visit(node.body_node, context)))
            if res.error:
                return res

        return res.success(List(elements).set_context(context).set_pos(node.pos_start, node.pos_end))

    def visit_WhileNode(self, node, context: Context) -> RTResult:
        """Evaluate a while loop expression.

        Args:
            node: The WhileNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the List value on completion, or an error.
        """
        res = RTResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition_node, context))
            if res.error:
                return res

            if not condition.is_true():
                break

            elements.append(res.register(self.visit(node.body_node, context)))
            if res.error:
                return res

        return res.success(List(elements).set_context(context).set_pos(node.pos_start, node.pos_end))

    def visit_FuncDefNode(self, node, context: Context) -> RTResult:
        """Evaluate a function definition expression.

        Creates a Function value and optionally binds it to a name
        in the current scope (for named functions).

        Args:
            node: The FuncDefNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the Function value.
        """
        res = RTResult()

        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        func_value = Function(func_name, body_node, arg_names).set_context(
            context
        ).set_pos(node.pos_start, node.pos_end)

        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)

        return res.success(func_value)

    def visit_CallNode(self, node, context: Context) -> RTResult:
        """Evaluate a function call expression.

        Resolves the callable, evaluates all arguments, and executes
        the function.

        Args:
            node: The CallNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the function's return value, or an error.
        """
        res = RTResult()
        args = []

        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.error:
            return res
        value_to_call = value_to_call.copy().set_pos(node.pos_start, node.pos_end)

        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))
            if res.error:
                return res

        return_value = res.register(value_to_call.execute(args))
        if res.error:
            return res
        return res.success(return_value)

    def visit_ListNode(self, node, context: Context) -> RTResult:
        """Evaluate a list literal node.

        Args:
            node: The ListNode to evaluate.
            context: The current execution context.

        Returns:
            An RTResult containing the List value.
        """
        res = RTResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.error:
                return res

        return res.success(List(elements).set_pos(node.pos_start, node.pos_end))
