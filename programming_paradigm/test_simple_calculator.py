import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(3, 6), -3)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 6), 18)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Test the addition by zero method."""
        self.assertIsNone(self.calc.divide(10, 0), None)


if __name__ == "__main__":
    unittest.main()
