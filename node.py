# Number Node - Just an integer or float
class NumberNode:
    # tok -> a number Token
    # pos_start -> the node itself
    # pos_end -> also the node itself
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


### Binary Operation Node - Add/Multiply/Subtract/Divide of two nodes ###
class BinOpNode:
    # left_node -> a number Token
    # op_tok -> an operator Token
    # right_node -> a number Token
    # pos_start -> the left nodes start
    # pos_end -> the right nodes end
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


### Unary Operation Node - (Ex: -5) ###
class UnaryOpNode:
    # op_token -> an operator Token
    # node -> a number Token
    # pos_start -> start (will be the operator (-5)
    # pos_end -> the node itself
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'


# Will hold saved variables
class VarAccessNode:
    # var_name_tok -> variable name
    # pos_start -> start of SHOW token
    # pos_end -> the end of variable name itself
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end


# will hold variable assignment
class VarAssignNode:
    # var_name_tok -> variable name
    # value_node -> variables value
    # pos_start -> start of variable name
    # pos_end -> the value nodes end position
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end


# Node that will be used to run scripts
class VarRunNode:
    # var_run_tok -> token to run script
    # pos_start -> start of simc token
    # pos_end -> the end of file name
    def __init__(self, var_run_tok):
        self.var_run_tok = var_run_tok
        self.pos_start = self.var_run_tok.pos_start
        self.pos_end = self.var_run_tok.pos_end
