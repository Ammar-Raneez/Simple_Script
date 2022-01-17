# Keep track of Lexer position
class Position:
    # index -> int index of the position
    # ln_number -> int line number of the position
    # col_number -> int column number of the position
    # f_name -> string file name of the position
    # f_text -> string text (input)
    def __init__(self, index, ln_number, col_number, f_name, f_text):
        self.index = index
        self.lnNumber = ln_number
        self.colNumber = col_number
        self.fName = f_name
        self.fText = f_text

    def advance(self, current_char=None):
        self.index += 1
        self.colNumber += 1

        # set col number to zero on a new line
        if current_char == '\n':
            self.lnNumber += 1
            self.colNumber = 0
        return self

    def copy(self):
        return Position(self.index, self.lnNumber, self.colNumber, self.fName, self.fText)
