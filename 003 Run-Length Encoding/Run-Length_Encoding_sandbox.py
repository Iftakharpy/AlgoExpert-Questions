# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = program.runLengthEncoding(string)
        self.assertEqual(actual, expected)
