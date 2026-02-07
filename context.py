### Context - Will trace runtime errors ###
class Context:
    # display_name -> the context itself
    # parent -> any parent of the place where the error occurred
    # For functions, the function that calls the error would be the parent, whose parent would be the python module itself
    # parent_entry_pos -> location where the error was called by the parent (Ex: line 2)
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
