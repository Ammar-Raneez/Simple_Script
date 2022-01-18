from error import RTError


# keep track of the result
class Number:
    # pos_start -> Position of the start of the number
    # pos_end -> Position of the end of the number
    # value -> the actual value of the number
    def __init__(self, value):
        self.context = None
        self.pos_end = None
        self.pos_start = None
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    # add a number - cannot have errors
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    # subtract by a number - cannot have errors
    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

    # multiplied by a number - cannot have errors
    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    # divided by a number - possible to have divided by 0 error
    def dived_by(self, other):
        if isinstance(other, Number):
            # disallow divisions by zero
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )

            return Number(self.value / other.value).set_context(self.context), None

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
