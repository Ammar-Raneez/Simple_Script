import unittest
from simple_script import run
from error import *


class UnitTest(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)

    def test_b(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10')
        self.assertEqual('10', str(returned_val))

    def test_c(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('10', str(returned_val))

    def test_d(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10^2')
        self.assertEqual('100', str(returned_val))

    def test_e(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('100', str(returned_val))

    def test_f(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10*5+2')
        self.assertEqual('52', str(returned_val))

    def test_g(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('52', str(returned_val))

    def test_h(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10*(5+2)')
        self.assertEqual('70', str(returned_val))

    def test_i(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('70', str(returned_val))

    def test_j(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 2 == 2 AND 4 == 5')
        self.assertEqual('0', str(returned_val))

    def test_k(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 2 == 2 AND 5 == 5')
        self.assertEqual('1', str(returned_val))

    def test_l(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = IF 2==5 THEN 2 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_m(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = IF 2==5 THEN 2 ELIF 3==5 THEN 3 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_n(self):
        run('<stdin>', 'VAR A = 10+5')
        returned_val, returned_err = run('<stdin>', f'VAR B = A+5')
        self.assertEqual('20', str(returned_val))

    def test_o(self):
        run('<stdin>', 'VAR A = IF 10+5 == 15 THEN 15 ELSE 0')
        returned_val, returned_err = run('<stdin>', f'VAR B = A+5')
        self.assertEqual('20', str(returned_val))

    def test_p(self):
        run('<stdin>', 'VAR A = 1')
        run('<stdin>', f'FOR i=1 TO 6 THEN VAR A = A*i')
        self.assertEqual('120', str(run('<stdin>', 'SHOW A')[0]))

    def test_q(self):
        run('<stdin>', 'VAR A = 1')
        run('<stdin>', f'FOR i=5 TO 0 STEP -1 THEN VAR A = A*i')
        self.assertEqual('120', str(run('<stdin>', 'SHOW A')[0]))

    def test_r(self):
        run('<stdin>', 'VAR A = 10')
        run('<stdin>', f'WHILE A < 50 THEN VAR A = A+1')
        self.assertEqual('50', str(run('<stdin>', 'SHOW A')[0]))

    def test_error_a(self):
        returned_val, returned_err = run('<stdin>', 'VARA 10')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, InvalidSyntaxError)

    def test_error_b(self):
        returned_val, returned_err = run('<stdin>', 'SHOW B')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_error_c(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10$')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, IllegalCharError)

    def test_error_d(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10/0')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_error_e(self):
        returned_val, returned_err = run('<stdin>', 'VAR A = 10 + C')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    # Function tests
    def test_func_a(self):
        # Test simple function definition and call
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(5, 3)')
        self.assertEqual('8', str(returned_val))

    def test_func_b(self):
        # Test function with single parameter
        run('<stdin>', 'VAR square = FUNC(x) -> x * x')
        returned_val, returned_err = run('<stdin>', 'square(7)')
        self.assertEqual('49', str(returned_val))

    def test_func_c(self):
        # Test function with no parameters
        run('<stdin>', 'VAR get_ten = FUNC() -> 10')
        returned_val, returned_err = run('<stdin>', 'get_ten()')
        self.assertEqual('10', str(returned_val))

    def test_func_d(self):
        # Test function with complex expression
        run('<stdin>', 'VAR calc = FUNC(x, y) -> x * 2 + y * 3')
        returned_val, returned_err = run('<stdin>', 'calc(5, 10)')
        self.assertEqual('40', str(returned_val))

    def test_func_e(self):
        # Test function that takes parameters
        run('<stdin>', 'VAR multiply = FUNC(x, multiplier) -> x * multiplier')
        returned_val, returned_err = run('<stdin>', 'multiply(5, 10)')
        self.assertEqual('50', str(returned_val))

    def test_func_f(self):
        # Test function with conditional logic
        run('<stdin>', 'VAR abs_val = FUNC(x) -> IF x < 0 THEN -x ELSE x')
        returned_val, returned_err = run('<stdin>', 'abs_val(-15)')
        self.assertEqual('15', str(returned_val))

    def test_func_g(self):
        # Test function with multiple operations
        run('<stdin>', 'VAR formula = FUNC(a, b, c) -> a^2 + b^2 + c^2')
        returned_val, returned_err = run('<stdin>', 'formula(3, 4, 5)')
        self.assertEqual('50', str(returned_val))

    def test_func_h(self):
        # Test storing function result in variable
        run('<stdin>', 'VAR subtract = FUNC(a, b) -> a - b')
        returned_val, returned_err = run('<stdin>', 'VAR result = subtract(20, 8)')
        self.assertEqual('12', str(returned_val))

    def test_func_i(self):
        # Test function with comparison operators
        run('<stdin>', 'VAR is_equal = FUNC(a, b) -> a == b')
        returned_val, returned_err = run('<stdin>', 'is_equal(5, 5)')
        self.assertEqual('1', str(returned_val))

    def test_func_j(self):
        # Test function with logical operators
        run('<stdin>', 'VAR and_func = FUNC(a, b) -> a AND b')
        returned_val, returned_err = run('<stdin>', 'and_func(1, 0)')
        self.assertEqual('0', str(returned_val))

    def test_func_error_a(self):
        # Test function call with too many arguments
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(1, 2, 3)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_func_error_b(self):
        # Test function call with too few arguments
        run('<stdin>', 'VAR add = FUNC(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(1)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_func_error_c(self):
        # Test calling undefined function
        returned_val, returned_err = run('<stdin>', 'undefined_func(5)')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_func_named_a(self):
        # Test named function definition and call
        run('<stdin>', 'FUNC add(a, b) -> a + b')
        returned_val, returned_err = run('<stdin>', 'add(5, 3)')
        self.assertEqual('8', str(returned_val))

    def test_func_named_b(self):
        # Test named function with single parameter
        run('<stdin>', 'FUNC square(x) -> x * x')
        returned_val, returned_err = run('<stdin>', 'square(9)')
        self.assertEqual('81', str(returned_val))

    def test_func_named_c(self):
        # Test named function with no parameters
        run('<stdin>', 'FUNC get_five() -> 5')
        returned_val, returned_err = run('<stdin>', 'get_five()')
        self.assertEqual('5', str(returned_val))

    def test_func_named_d(self):
        # Test named function with complex expression
        run('<stdin>', 'FUNC calc(x, y) -> x^2 + y^2')
        returned_val, returned_err = run('<stdin>', 'calc(3, 4)')
        self.assertEqual('25', str(returned_val))


if __name__ == '__main__':
    unittest.main()
