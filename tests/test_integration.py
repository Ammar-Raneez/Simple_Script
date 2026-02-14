"""Integration tests for the SimpleScript interpreter.

Tests the full pipeline from source code to result, covering variables,
arithmetic, comparisons, conditionals, loops, functions, and strings.
"""

import unittest
from simplescript.runtime import run
from simplescript.errors.errors import (
    InvalidSyntaxError,
    RTError,
    IllegalCharError,
)


class TestVariables(unittest.TestCase):
    """Tests for variable assignment and access."""

    def test_assign_integer(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10')
        self.assertEqual('10', str(returned_val))

    def test_access_variable(self):
        run('<stdin>', 'VAR A = 10')
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('10', str(returned_val))

    def test_assign_power(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10^2')
        self.assertEqual('100', str(returned_val))

    def test_assign_arithmetic(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10*5+2')
        self.assertEqual('52', str(returned_val))

    def test_assign_parenthesized(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10*(5+2)')
        self.assertEqual('70', str(returned_val))

    def test_assign_comparison_and(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 2 == 2 AND 4 == 5')
        self.assertEqual('0', str(returned_val))

    def test_assign_comparison_and_true(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 2 == 2 AND 5 == 5')
        self.assertEqual('1', str(returned_val))

    def test_assign_conditional(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = IF 2==5 THEN 2 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_assign_conditional_elif(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = IF 2==5 THEN 2 ELIF 3==5 THEN 3 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_variable_in_expression(self):
        run('<stdin>', 'VAR A = 10+5')
        returned_val, returned_err = run('<stdin>', 'VAR B = A+5')
        self.assertEqual('20', str(returned_val))

    def test_variable_from_conditional(self):
        run('<stdin>', 'VAR A = IF 10+5 == 15 THEN 15 ELSE 0')
        returned_val, returned_err = run('<stdin>', 'VAR B = A+5')
        self.assertEqual('20', str(returned_val))


class TestLoops(unittest.TestCase):
    """Tests for for and while loops."""

    def test_for_loop_factorial(self):
        run('<stdin>', 'VAR A = 1')
        run('<stdin>', 'FOR i=1 TO 6 THEN VAR A = A*i')
        self.assertEqual('120', str(run('<stdin>', 'SHOW A')[0]))

    def test_for_loop_step(self):
        run('<stdin>', 'VAR A = 1')
        run('<stdin>', 'FOR i=5 TO 0 STEP -1 THEN VAR A = A*i')
        self.assertEqual('120', str(run('<stdin>', 'SHOW A')[0]))

    def test_while_loop(self):
        run('<stdin>', 'VAR A = 10')
        run('<stdin>', 'WHILE A < 50 THEN VAR A = A+1')
        self.assertEqual('50', str(run('<stdin>', 'SHOW A')[0]))


class TestFunctionsAnonymous(unittest.TestCase):
    """Tests for anonymous function definitions and calls."""

    def test_simple_add(self):
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(5, 3)')
        self.assertEqual('8', str(returned_val))

    def test_single_param(self):
        run('<stdin>', 'VAR square = FUNC(x) -> x * x')
        returned_val, returned_err = run('<stdin>', 'square(7)')
        self.assertEqual('49', str(returned_val))

    def test_no_params(self):
        run('<stdin>', 'VAR get_ten = FUNC() -> 10')
        returned_val, returned_err = run('<stdin>', 'get_ten()')
        self.assertEqual('10', str(returned_val))

    def test_complex_expression(self):
        run('<stdin>', 'VAR calc = FUNC(x, y) -> x * 2 + y * 3')
        returned_val, returned_err = run('<stdin>', 'calc(5, 10)')
        self.assertEqual('40', str(returned_val))

    def test_multiple_params(self):
        run('<stdin>', 'VAR multiply = FUNC(x, multiplier) -> x * multiplier')
        returned_val, returned_err = run('<stdin>', 'multiply(5, 10)')
        self.assertEqual('50', str(returned_val))

    def test_conditional_body(self):
        run('<stdin>', 'VAR abs_val = FUNC(x) -> IF x < 0 THEN -x ELSE x')
        returned_val, returned_err = run('<stdin>', 'abs_val(-15)')
        self.assertEqual('15', str(returned_val))

    def test_multiple_operations(self):
        run('<stdin>', 'VAR formula = FUNC(a, b, c) -> a^2 + b^2 + c^2')
        returned_val, returned_err = run('<stdin>', 'formula(3, 4, 5)')
        self.assertEqual('50', str(returned_val))

    def test_store_result(self):
        run('<stdin>', 'VAR subtract = FUNC(a, b) -> a - b')
        returned_val, returned_err = run('<stdin>', 'VAR result = subtract(20, 8)')
        self.assertEqual('12', str(returned_val))

    def test_comparison(self):
        run('<stdin>', 'VAR is_equal = FUNC(a, b) -> a == b')
        returned_val, returned_err = run('<stdin>', 'is_equal(5, 5)')
        self.assertEqual('1', str(returned_val))

    def test_logical_operator(self):
        run('<stdin>', 'VAR and_func = FUNC(a, b) -> a AND b')
        returned_val, returned_err = run('<stdin>', 'and_func(1, 0)')
        self.assertEqual('0', str(returned_val))


class TestFunctionsNamed(unittest.TestCase):
    """Tests for named function definitions and calls."""

    def test_named_add(self):
        run('<stdin>', 'FUNC add(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(5, 3)')
        self.assertEqual('8', str(returned_val))

    def test_named_single_param(self):
        run('<stdin>', 'FUNC square(x) -> x * x')
        returned_val, returned_err = run('<stdin>', 'square(9)')
        self.assertEqual('81', str(returned_val))

    def test_named_no_params(self):
        run('<stdin>', 'FUNC get_five() -> 5')
        returned_val, returned_err = run('<stdin>', 'get_five()')
        self.assertEqual('5', str(returned_val))

    def test_named_complex(self):
        run('<stdin>', 'FUNC calc(x, y) -> x^2 + y^2')
        returned_val, returned_err = run('<stdin>', 'calc(3, 4)')
        self.assertEqual('25', str(returned_val))


class TestStrings(unittest.TestCase):
    """Tests for string literals and operations."""

    def test_simple_string(self):
        returned_val, returned_err = run('<stdin>', '"hello"')
        self.assertEqual('"hello"', str(returned_val))
        self.assertEqual('hello', returned_val.value)

    def test_concatenation(self):
        returned_val, returned_err = run('<stdin>', '"hello" + " " + "world"')
        self.assertEqual('"hello world"', str(returned_val))

    def test_escaped_quotes(self):
        returned_val, returned_err = run('<stdin>', r'"I said \"hello\""')
        self.assertEqual('"I said "hello""', str(returned_val))
        self.assertEqual('I said "hello"', returned_val.value)

    def test_escaped_newline(self):
        returned_val, returned_err = run('<stdin>', r'"line1\nline2"')
        self.assertEqual('line1\nline2', returned_val.value)

    def test_escaped_tab(self):
        returned_val, returned_err = run('<stdin>', r'"tab\there"')
        self.assertEqual('tab\there', returned_val.value)

    def test_escaped_backslash(self):
        returned_val, returned_err = run('<stdin>', r'"back\\slash"')
        self.assertEqual('back\\slash', returned_val.value)

    def test_multiplication(self):
        returned_val, returned_err = run('<stdin>', '"ha" * 3')
        self.assertEqual('"hahaha"', str(returned_val))

    def test_in_variable(self):
        run('<stdin>', 'VAR greeting = "Hello World"')
        returned_val, returned_err = run('<stdin>', 'SHOW greeting')
        self.assertEqual('"Hello World"', str(returned_val))

    def test_in_conditional(self):
        returned_val, returned_err = run('<stdin>', 'IF 1 == 1 THEN "yes" ELSE "no"')
        self.assertEqual('"yes"', str(returned_val))

    def test_empty_string(self):
        returned_val, returned_err = run('<stdin>', '""')
        self.assertEqual('""', str(returned_val))
        self.assertEqual('', returned_val.value)

    def test_multiple_escaped_quotes(self):
        returned_val, returned_err = run('<stdin>', r'"\"quoted\" text"')
        self.assertEqual('"quoted" text', returned_val.value)

    def test_with_function(self):
        run('<stdin>', 'FUNC greet(name) -> "Hello, " + name')
        returned_val, returned_err = run('<stdin>', 'greet("Alice")')
        self.assertEqual('"Hello, Alice"', str(returned_val))

    def test_single_quotes(self):
        returned_val, returned_err = run('<stdin>', "'hello'")
        self.assertEqual('"hello"', str(returned_val))
        self.assertEqual('hello', returned_val.value)

    def test_single_quotes_with_double_inside(self):
        returned_val, returned_err = run('<stdin>', "'He said \"hi\"'")
        self.assertEqual('He said "hi"', returned_val.value)

    def test_double_quotes_with_single_inside(self):
        returned_val, returned_err = run('<stdin>', '"I\'m happy"')
        self.assertEqual("I'm happy", returned_val.value)

    def test_escaped_single_quote(self):
        returned_val, returned_err = run('<stdin>', r"'don\'t'")
        self.assertEqual("don't", returned_val.value)

    def test_mixed_concatenation(self):
        returned_val, returned_err = run('<stdin>', "'hello' + \" \" + \"world\"")
        self.assertEqual('"hello world"', str(returned_val))


class TestLists(unittest.TestCase):
    """Tests for list literals and operations."""

    def test_empty_list(self):
        returned_val, returned_err = run('<stdin>', '[]')
        self.assertEqual('[]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_integers(self):
        returned_val, returned_err = run('<stdin>', '[1, 2, 3]')
        self.assertEqual('[1, 2, 3]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_strings(self):
        returned_val, returned_err = run('<stdin>', '["hello", "world"]')
        self.assertEqual('["hello", "world"]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_mixed_types(self):
        returned_val, returned_err = run('<stdin>', '[1, "hello", 3.5]')
        self.assertEqual('[1, "hello", 3.5]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_expressions(self):
        returned_val, returned_err = run('<stdin>', '[1 + 2, 5 * 3, 10 - 4]')
        self.assertEqual('[3, 15, 6]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_nested_lists(self):
        returned_val, returned_err = run('<stdin>', '[[1, 2], [3, 4]]')
        self.assertEqual('[[1, 2], [3, 4]]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_in_variable(self):
        run('<stdin>', 'VAR mylist = [10, 20, 30]')
        returned_val, returned_err = run('<stdin>', 'SHOW mylist')
        self.assertEqual('[10, 20, 30]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_append(self):
        returned_val, returned_err = run('<stdin>', '[1, 2, 3] + 4')
        self.assertEqual('[1, 2, 3, 4]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_append_string(self):
        returned_val, returned_err = run('<stdin>', '["a", "b"] + "c"')
        self.assertEqual('["a", "b", "c"]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_extend(self):
        returned_val, returned_err = run('<stdin>', '[1, 2] * [3, 4]')
        self.assertEqual('[1, 2, 3, 4]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_get_element(self):
        returned_val, returned_err = run('<stdin>', '[10, 20, 30] / 0')
        self.assertEqual('10', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_get_element_last(self):
        returned_val, returned_err = run('<stdin>', '[10, 20, 30] / 2')
        self.assertEqual('30', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_remove_element(self):
        returned_val, returned_err = run('<stdin>', '[10, 20, 30] - 1')
        self.assertEqual('[10, 30]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_remove_first_element(self):
        returned_val, returned_err = run('<stdin>', '[10, 20, 30] - 0')
        self.assertEqual('[20, 30]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_in_conditional(self):
        returned_val, returned_err = run('<stdin>', 'IF 1 == 1 THEN [1, 2, 3] ELSE [4, 5, 6]')
        self.assertEqual('[1, 2, 3]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_function(self):
        run('<stdin>', 'FUNC get_list() -> [1, 2, 3]')
        returned_val, returned_err = run('<stdin>', 'get_list()')
        self.assertEqual('[1, 2, 3]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_operations_in_variable(self):
        run('<stdin>', 'VAR list1 = [1, 2]')
        returned_val, returned_err = run('<stdin>', 'VAR list2 = list1 + 3')
        self.assertEqual('[1, 2, 3]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_extend_variables(self):
        run('<stdin>', 'VAR list1 = [1, 2]')
        run('<stdin>', 'VAR list2 = [3, 4]')
        returned_val, returned_err = run('<stdin>', 'list1 * list2')
        self.assertEqual('[1, 2, 3, 4]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_single_element(self):
        returned_val, returned_err = run('<stdin>', '[42]')
        self.assertEqual('[42]', str(returned_val))
        self.assertIsNone(returned_err)

    def test_list_with_nested_expressions(self):
        returned_val, returned_err = run('<stdin>', '[1, 2 + 3, 4 * 5]')
        self.assertEqual('[1, 5, 20]', str(returned_val))
        self.assertIsNone(returned_err)


class TestListErrors(unittest.TestCase):
    """Tests for list error handling."""

    def test_list_index_out_of_bounds(self):
        returned_val, returned_err = run('<stdin>', '[1, 2, 3] / 5')
        self.assertIsNone(returned_val)
        self.assertIsInstance(returned_err, RTError)
        self.assertIn('out of bounds', returned_err.details)

    def test_list_remove_index_out_of_bounds(self):
        returned_val, returned_err = run('<stdin>', '[1, 2, 3] - 10')
        self.assertIsNone(returned_val)
        self.assertIsInstance(returned_err, RTError)
        self.assertIn('out of bounds', returned_err.details)

    def test_list_negative_index(self):
        # Python allows negative indexing, so -1 gets the last element
        returned_val, returned_err = run('<stdin>', '[1, 2, 3] / -1')
        self.assertEqual('3', str(returned_val))
        self.assertIsNone(returned_err)

    def test_empty_list_index(self):
        returned_val, returned_err = run('<stdin>', '[] / 0')
        self.assertIsNone(returned_val)
        self.assertIsInstance(returned_err, RTError)


class TestErrors(unittest.TestCase):
    """Tests for error handling."""

    def test_invalid_syntax(self):
        returned_val, returned_err = run('<stdin>', 'VARA 10')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, InvalidSyntaxError)

    def test_undefined_variable(self):
        returned_val, returned_err = run('<stdin>', 'SHOW B')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_illegal_character(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10$')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, IllegalCharError)

    def test_division_by_zero(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10/0')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_undefined_in_expression(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10 + C')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_too_many_args(self):
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(1, 2, 3)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_too_few_args(self):
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(1)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_undefined_function(self):
        returned_val, returned_err = run('<stdin>', 'undefined_func(5)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)


if __name__ == '__main__':
    unittest.main()
