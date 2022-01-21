import unittest
from simple_script import run
from error import *


class UnitTest(unittest.TestCase):
    def test_always_true(self):
        self.assertTrue(True)

    def test_simple_save(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10')
        self.assertEqual('10', str(returned_val))

    def test_simple_show(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('10', str(returned_val))

    def test_intermediate_save(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10^2')
        self.assertEqual('100', str(returned_val))

    def test_intermediate_show(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('100', str(returned_val))

    def test_advanced_save(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10*5+2')
        self.assertEqual('52', str(returned_val))

    def test_advanced_show(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('52', str(returned_val))

    def test_expert_save(self):
        returned_val, returned_err = run('<stdin>', 'SAVE A 10*(5+2)')
        self.assertEqual('70', str(returned_val))

    def test_expert_show(self):
        returned_val, returned_err = run('<stdin>', 'SHOW A')
        self.assertEqual('70', str(returned_val))

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
