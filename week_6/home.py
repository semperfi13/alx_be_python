import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(5, 7)
        self.assertEqual(result, 12)

    def test_add_negative(self):
        result = add(-9, -12)
        self.assertEqual(result, -21)


if __name__ == "__main__":
    unittest.main()
