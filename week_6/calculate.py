import unittest


def calculate(a):
    return a - a


class Test(unittest.TestCase):
    def test_calculate(self):
        result = calculate(20)
        self.assertEqual(result, 400)

    def test_calculate_negative(self):
        result = calculate(20)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
