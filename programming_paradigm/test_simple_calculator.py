import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero
        self.assertEqual(self.calc.divide(-6, -2), 3)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_float(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)
        self.assertAlmostEqual(self.calc.divide(7.0, 0.0), None)
        self.assertAlmostEqual(self.calc.divide(-3.6, -1.2), 3.0)
    def test_divide_large_numbers(self):
        self.assertEqual(self.calc.divide(1e6, 1e3), 1000)
        self.assertEqual(self.calc.divide(1e6, 0), None)
        self.assertEqual(self.calc.divide(-1e6, -1e3), 1000)
if __name__ == '__main__':
    unittest.main()