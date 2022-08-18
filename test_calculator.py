import unittest
import calculator

class TestCalculatorOperators(unittest.TestCase):

    def test_make_sum(self):
        """Sum values and return the result"""
        assert calculator.make_sum(1,2) == 3