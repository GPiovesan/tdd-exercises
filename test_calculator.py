import unittest
import calculator

class TestCalculatorOperators(unittest.TestCase):

    def test_sum_two_values(self):
        """Sum the values and return the result"""
        assert calculator.sum(1,2) == 3

    def test_sub_two_values(self):
        """Subtract the values and return the result"""
        assert calculator.subtract(1, 2) == -1

    def test_div_two_values(self):
        """Get the first number and divide by the second"""
        assert calculator.divide(3, 2) == 1.5

    def test_multiply_two_values(self):
        """Multiply the numbers and return the result"""
        assert calculator.multiply(4, 2) == 8