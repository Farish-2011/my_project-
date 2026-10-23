import unittest
from calculator import add, subtract,multiplication, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,8),10)
    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
    def test_multiply(self):
        self.assertEqual(multiplication(6,3),18)
    def test_divide_by_0(self):
        with self.assertRaises(ValueError):
            divide(10,0)

if __name__ == "__main__":
    unittest.main()