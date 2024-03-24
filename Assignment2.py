# Chelsea Rowe
import unittest


class Arithmetic:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Cannot divide by 0."


class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.arithmetic = Arithmetic()

    def test_addition(self):
        self.assertEqual(self.arithmetic.addition(1, 2), 3)
        self.assertNotEqual(self.arithmetic.addition(1, 2), 4)
        self.assertTrue(self.arithmetic.addition(1, 2) == 3)
        self.assertFalse(self.arithmetic.addition(1, 2) != 3)

    def test_subtraction(self):
        self.assertEqual(self.arithmetic.subtraction(10, 5), 5)
        self.assertNotEqual(self.arithmetic.subtraction(10, 5), 1)
        self.assertTrue(self.arithmetic.subtraction(5, 3) == 2)
        self.assertFalse(self.arithmetic.subtraction(5, 3) != 2)

    def test_multiplication(self):
        self.assertEqual(self.arithmetic.multiplication(3, 2), 6)
        self.assertNotEqual(self.arithmetic.multiplication(3, 2), 10)
        self.assertTrue(self.arithmetic.multiplication(3, 5) == 15)
        self.assertFalse(self.arithmetic.multiplication(3, 5) != 15)

    def test_division(self):
        self.assertEqual(self.arithmetic.division(10, 2), 5)
        self.assertNotEqual(self.arithmetic.division(10, 2), 3)
        self.assertTrue(self.arithmetic.division(10, 2) == 5)
        self.assertFalse(self.arithmetic.division(10, 2) != 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
