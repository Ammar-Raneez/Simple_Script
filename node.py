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


# Will hold VARd variables
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


# Node that will be used to hold if conditions
class IfNode:
    # cases -> list of conditions with their expressions
    # else_case -> if else statement present, will hold it
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case
        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1][0]).pos_end


# For loop node
class ForNode:
    # var_name_tok -> variable name
    # start_value_node -> start of loop
    # end_value_node -> end of loop
    # step_value_node -> step counter
    # body_node -> body of loop
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end


# While loop node
class WhileNode:
    # condition_node -> while loop condition
    # body_node -> body of loop
    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end


# Function definition node
class FuncDefNode:
    # var_name_tok -> variable name
    # arg_name_toks -> list of argument names
    # body_node -> body of function
	def __init__(self, var_name_tok, arg_name_toks, body_node):
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

# Function call node
class CallNode:
    # node_to_call -> function to call
    # arg_nodes -> list of argument nodes
	def __init__(self, node_to_call, arg_nodes):
		self.node_to_call = node_to_call
		self.arg_nodes = arg_nodes

		self.pos_start = self.node_to_call.pos_start

		if len(self.arg_nodes) > 0:
			self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
		else:
			self.pos_end = self.node_to_call.pos_end