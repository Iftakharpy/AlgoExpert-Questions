# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
