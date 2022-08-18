import unittest
import calculator

class TestCalculatorOperators(unittest.TestCase):

    def test_sum_two_values(self):
        """Sum the values and return the result"""
        assert calculator.make_sum(1,2) == 3