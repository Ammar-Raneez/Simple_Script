import unittest
from simple_script import run
from error import *


class UnitTest(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)

    def test_b(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10')
        self.assertEqual('10', str(returned_val))

    def test_c(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('10', str(returned_val))

    def test_d(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10^2')
        self.assertEqual('100', str(returned_val))

    def test_e(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('100', str(returned_val))

    def test_f(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10*5+2')
        self.assertEqual('52', str(returned_val))

    def test_g(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('52', str(returned_val))

    def test_h(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10*(5+2)')
        self.assertEqual('70', str(returned_val))

    def test_i(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('70', str(returned_val))

    def test_j(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 2 == 2 AND 4 == 5')
        self.assertEqual('0', str(returned_val))

    def test_k(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 2 == 2 AND 5 == 5')
        self.assertEqual('1', str(returned_val))

    def test_l(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A IF 2==5 THEN 2 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_m(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A IF 2==5 THEN 2 ELIF 3==5 THEN 3 ELSE 5')
        self.assertEqual('5', str(returned_val))

    def test_error_a(self):
        returned_val, returned_err = run('<stdin>', 'SAVEA 10')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, InvalidSyntaxError)

    def test_error_b(self):
        returned_val, returned_err = run('<stdin>', 'SHOW B')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, RTError)

    def test_error_c(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10$')
        self.assertEqual(None, returned_val)
        self.assertIsInstance(returned_err, IllegalCharError)


if __name__ == '__main__':
    unittest.main()
