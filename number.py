from error import RTError
from value import Value


# keep track of the result
class Number(Value):
    # pos_start -> Position of the start of the number
    # pos_end -> Position of the end of the number
    # value -> the actual value of the number
    def __init__(self, value):
        super().__init__()
        self.value = value

    # add a number - cannot have errors
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

        return None, self.illegal_operation(other)

    # subtract by a number - cannot have errors
    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

        return None, self.illegal_operation(other)

    # multiplied by a number - cannot have errors
    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

        return None, self.illegal_operation(other)

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

        return None, self.illegal_operation(other)

    # powered by a number
    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None

        return None, self.illegal_operation(other)

    # equality comparison to a number
    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # not equal comparison to a number
    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # less than comparison to a number
    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # greater than comparison to a number
    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # less than or equal to comparison to a number
    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # greater than or equal to comparison to a number
    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # AND logic with a number
    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # OR logic with a number
    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None

        return None, self.illegal_operation(other)

    # ! logic with the number
    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    # check if true
    def is_true(self):
        return self.value != 0

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
