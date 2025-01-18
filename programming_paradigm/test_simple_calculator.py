import unittest
from simple_calculator import SimpleCalculator


class TestClass(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_additio(self):
        result = self.calc.add(3, 6)
        self.assertEqual(result, 9)

    def test_subtract(self):
        result = self.calc.subtract(3, 6)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = self.calc.multiply(3, 6)
        self.assertEqual(result, 18)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0), None)


if __name__ == "__main__":
    unittest.main()
