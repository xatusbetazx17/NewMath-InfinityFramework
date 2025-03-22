import unittest
from new_math import NewMath

class TestNewMath(unittest.TestCase):
    def setUp(self):
        self.nm = NewMath()

    # Division
    def test_divide_by_zero(self):
        self.assertEqual(self.nm.divide(10, 0), float("inf"))

    def test_zero_divided_by_zero(self):
        self.assertEqual(self.nm.divide(0, 0), "Undefined")

    def test_divide_infinity_by_number(self):
        self.assertEqual(self.nm.divide(self.nm.infinity, 5), float("inf"))

    def test_divide_number_by_infinity(self):
        self.assertEqual(self.nm.divide(5, self.nm.infinity), 0)

    # Addition
    def test_add_infinity(self):
        self.assertEqual(self.nm.add(5, self.nm.infinity), float("inf"))

    # Subtraction
    def test_subtract_infinity_from_infinity(self):
        self.assertEqual(self.nm.subtract(self.nm.infinity, self.nm.infinity), "Undefined")

    def test_subtract_finite_from_infinity(self):
        self.assertEqual(self.nm.subtract(self.nm.infinity, 10), float("inf"))

    # Multiplication
    def test_multiply_with_zero_and_infinity(self):
        self.assertEqual(self.nm.multiply(0, self.nm.infinity), 0)

    def test_multiply_finite_with_infinity(self):
        self.assertEqual(self.nm.multiply(2, self.nm.infinity), float("inf"))

    # Exponentiation
    def test_exponentiate_infinity_to_zero(self):
        self.assertEqual(self.nm.exponentiate(self.nm.infinity, 0), 1)

    def test_exponentiate_small_base_to_infinity(self):
        self.assertEqual(self.nm.exponentiate(0.5, self.nm.infinity), 0)

    def test_exponentiate_large_base_to_infinity(self):
        self.assertEqual(self.nm.exponentiate(2, self.nm.infinity), float("inf"))

if __name__ == "__main__":
    unittest.main()
