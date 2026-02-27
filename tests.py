import unittest
from main import add_positive_integers

class TestMathFunctions(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(add_positive_integers(5, 10), 15)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            add_positive_integers(-1, 5)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            add_positive_integers("5", 5)

if __name__ == "__main__":
    unittest.main()