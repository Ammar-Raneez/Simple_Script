"""Abstract Syntax Tree (AST) node definitions for SimpleScript.

This module defines all AST node types produced by the parser and
consumed by the interpreter. Each node type represents a different
syntactic construct in the SimpleScript language.
"""


class NumberNode:
    """AST node representing a numeric literal (integer or float).

    Args:
        tok: The number token from the lexer.

    Attributes:
        tok (Token): The number token containing the numeric value.
        pos_start (Position): Start position of the number in source text.
        pos_end (Position): End position of the number in source text.
    """

    def __init__(self, tok) -> None:
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self) -> str:
        return f"{self.tok}"


class StringNode:
    """AST node representing a string literal.

    Args:
        tok: The string token from the lexer.

    Attributes:
        tok (Token): The string token containing the string value.
        pos_start (Position): Start position of the string in source text.
        pos_end (Position): End position of the string in source text.
    """

    def __init__(self, tok) -> None:
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self) -> str:
        return f"{self.tok}"


class BinOpNode:
    """AST node representing a binary operation (e.g., addition, comparison).

    Args:
        left_node: The left operand node.
        op_tok: The operator token.
        right_node: The right operand node.

    Attributes:
        left_node: Left operand AST node.
        op_tok (Token): The operator token.
        right_node: Right operand AST node.
        pos_start (Position): Start position (from left operand).
        pos_end (Position): End position (from right operand).
    """

    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self) -> str:
        return f"({self.left_node}, {self.op_tok}, {self.right_node})"


class UnaryOpNode:
    """AST node representing a unary operation (e.g., negation).

    Args:
        op_tok: The operator token (e.g., minus sign).
        node: The operand node.

    Attributes:
        op_tok (Token): The unary operator token.
        node: The operand AST node.
        pos_start (Position): Start position (from the operator).
        pos_end (Position): End position (from the operand).
    """

    def __init__(self, op_tok, node) -> None:
        self.op_tok = op_tok
        self.node = node
        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self) -> str:
        return f"({self.op_tok}, {self.node})"


class VarAccessNode:
    """AST node representing a variable access expression.

    Args:
        var_name_tok: The identifier token for the variable name.

    Attributes:
        var_name_tok (Token): The variable name token.
        pos_start (Position): Start position of the identifier.
        pos_end (Position): End position of the identifier.
    """

    def __init__(self, var_name_tok) -> None:
        self.var_name_tok = var_name_tok
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end


class VarAssignNode:
    """AST node representing a variable assignment statement.

    Args:
        var_name_tok: The identifier token for the variable name.
        value_node: The AST node for the value expression.

    Attributes:
        var_name_tok (Token): The variable name token.
        value_node: The value expression AST node.
        pos_start (Position): Start position (from the variable name).
        pos_end (Position): End position (from the value expression).
    """

    def __init__(self, var_name_tok, value_node) -> None:
        self.var_name_tok = var_name_tok
        self.value_node = value_node
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end


class IfNode:
    """AST node representing an if/elif/else conditional expression.

    Args:
        cases: List of (condition, expression) tuples for if/elif branches.
        else_case: The expression for the else branch, or None.

    Attributes:
        cases (list): List of (condition_node, expr_node) tuples.
        else_case: The else branch expression node, or None.
        pos_start (Position): Start position (from the first condition).
        pos_end (Position): End position (from the last branch).
    """

    def __init__(self, cases: list, else_case=None) -> None:
        self.cases = cases
        self.else_case = else_case
        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1][0]).pos_end


class ForNode:
    """AST node representing a for loop.

    Args:
        var_name_tok: The loop variable identifier token.
        start_value_node: The starting value expression node.
        end_value_node: The ending value expression node.
        step_value_node: The step value expression node, or None for default.
        body_node: The loop body expression node.

    Attributes:
        var_name_tok (Token): The loop variable token.
        start_value_node: Start value AST node.
        end_value_node: End value AST node.
        step_value_node: Step value AST node, or None.
        body_node: Loop body AST node.
        pos_start (Position): Start position (from the variable name).
        pos_end (Position): End position (from the body).
    """

    def __init__(
        self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node
    ) -> None:
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end


class WhileNode:
    """AST node representing a while loop.

    Args:
        condition_node: The loop condition expression node.
        body_node: The loop body expression node.

    Attributes:
        condition_node: Condition AST node.
        body_node: Loop body AST node.
        pos_start (Position): Start position (from the condition).
        pos_end (Position): End position (from the body).
    """

    def __init__(self, condition_node, body_node) -> None:
        self.condition_node = condition_node
        self.body_node = body_node
        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end


class FuncDefNode:
    """AST node representing a function definition.

    Args:
        var_name_tok: The function name token, or None for anonymous functions.
        arg_name_toks: List of argument identifier tokens.
        body_node: The function body expression node.

    Attributes:
        var_name_tok (Optional[Token]): Function name token, or None.
        arg_name_toks (list[Token]): Argument name tokens.
        body_node: Function body AST node.
        pos_start (Position): Start position.
        pos_end (Position): End position (from the body).
    """

    def __init__(self, var_name_tok, arg_name_toks: list, body_node) -> None:
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node

        if self.var_name_tok:
            self.pos_start = self.var_name_tok.pos_start
        elif len(self.arg_name_toks) > 0:
            self.pos_start = self.arg_name_toks[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end


class CallNode:
    """AST node representing a function call.

    Args:
        node_to_call: The AST node resolving to the callable function.
        arg_nodes: List of argument expression nodes.

    Attributes:
        node_to_call: The callable AST node.
        arg_nodes (list): List of argument AST nodes.
        pos_start (Position): Start position (from the callable).
        pos_end (Position): End position (from the last argument or callable).
    """

    def __init__(self, node_to_call, arg_nodes: list) -> None:
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes
        self.pos_start = self.node_to_call.pos_start

        if len(self.arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end


class ListNode:
    """AST node representing a list.

    Args:
        element_nodes: List of element nodes.

    Attributes:
        element_nodes: List of element AST nodes.
        pos_start (Position): Start position (from the first element).
        pos_end (Position): End position (from the last element).
    """

    def __init__(self, element_nodes: list) -> None:
        self.element_nodes = element_nodes
        self.pos_start = (
            self.element_nodes[0].pos_start if len(self.element_nodes) > 0 else None
        )
        self.pos_end = (
            self.element_nodes[len(self.element_nodes) - 1].pos_end
            if len(self.element_nodes) > 0
            else None
        )


class MapNode:
    """AST node representing a map (dictionary) literal.

    Args:
        key_value_pairs: List of tuples containing (key_node, value_node) pairs.
        pos_start: Start position of the map.
        pos_end: End position of the map.

    Attributes:
        key_value_pairs: List of (key_node, value_node) tuples.
        pos_start (Position): Start position.
        pos_end (Position): End position.
    """

    def __init__(self, key_value_pairs: list, pos_start=None, pos_end=None) -> None:
        self.key_value_pairs = key_value_pairs
        self.pos_start = pos_start
        self.pos_end = pos_end
