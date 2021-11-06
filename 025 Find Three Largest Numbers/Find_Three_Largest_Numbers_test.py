from Find_Three_Largest_Numbers import findThreeLargestNumbers

def test_findThreeLargestNumbers_case_1():
    assert findThreeLargestNumbers(array=[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541]

def test_findThreeLargestNumbers_case_2():
    assert findThreeLargestNumbers(array=[55, 7, 8]) == [7, 8, 55]

def test_findThreeLargestNumbers_case_3():
    assert findThreeLargestNumbers(array=[55, 43, 11, 3, -3, 10]) == [11, 43, 55]

def test_findThreeLargestNumbers_case_4():
    assert findThreeLargestNumbers(array=[7, 8, 3, 11, 43, 55]) == [11, 43, 55]

def test_findThreeLargestNumbers_case_5():
    assert findThreeLargestNumbers(array=[55, 7, 8, 3, 43, 11]) == [11, 43, 55]

def test_findThreeLargestNumbers_case_6():
    assert findThreeLargestNumbers(array=[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7]

def test_findThreeLargestNumbers_case_7():
    assert findThreeLargestNumbers(array=[7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]) == [7, 7, 8]

def test_findThreeLargestNumbers_case_8():
    assert findThreeLargestNumbers(array=[-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]) == [-2, -1, 7]

