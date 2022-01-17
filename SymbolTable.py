# Will keep track of all the variables and their values
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def get(self, name):
        value = self.symbols.get(name, None)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]
