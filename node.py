### Number Node - Just an integer or float ###
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


# Will hold saved variable names
class VarAccessNode:
    # var_name_tok -> variable name
    # pos_start -> start of variable name
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
