# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
        expected = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
        actual = program.radixSort(input)
        self.assertEqual(actual, expected)
