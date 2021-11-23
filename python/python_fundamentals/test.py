import unittest
from unittest.mock import patch
from function_basics_2 import *


class TestFunBasTwo(unittest.TestCase):

    def test_countdown(self):
        self.assertEqual(countdown_v1(5), [5, 4, 3, 2, 1, 0])

    @patch('builtins.print')
    def test_print_and_return_print(self, mock_print):
        print_and_return([1, 2])
        mock_print.assert_called_with(1)

    def test_print_and_return_return(self):
        func = print_and_return([1, 2])
        self.assertEqual(func, 2)

    def test_first_plus_length(self):
        func = first_plus_length([1, 2, 3, 4, 5])
        self.assertEquals(func, 6)

    def test_values_greater_than_second(self):
        func = values_greater_than_second([5, 2, 3, 2, 1, 4])
        self.assertListEqual(func, [5, 3, 4])

    @patch('builtins.print')
    def test_values_greater_than_second_print(self, mock_print):
        values_greater_than_second([5, 2, 3, 2, 1, 4])
        mock_print.assert_called_with(3)

    def test_values_greater_than_second_boolean(self):
        func = values_greater_than_second([3])
        self.assertFalse(func)
