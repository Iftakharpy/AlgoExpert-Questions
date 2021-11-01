from Two_Number_Sum import twoNumberSum

def test_twoNumberSum_case_1():
    assert twoNumberSum(array=[3, 5, -4, 8, 11, 1, -1, 6], targetSum=10) == [11, -1]

def test_twoNumberSum_case_2():
    assert twoNumberSum(array=[4, 6], targetSum=10) == [4, 6]

def test_twoNumberSum_case_3():
    assert twoNumberSum(array=[4, 6, 1], targetSum=5) == [4, 1]

def test_twoNumberSum_case_4():
    assert twoNumberSum(array=[4, 6, 1, -3], targetSum=3) == [6, -3]

def test_twoNumberSum_case_5():
    assert twoNumberSum(array=[1, 2, 3, 4, 5, 6, 7, 8, 9], targetSum=17) == [8, 9]

def test_twoNumberSum_case_6():
    assert twoNumberSum(array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], targetSum=18) == [3, 15]

def test_twoNumberSum_case_7():
    assert twoNumberSum(array=[-7, -5, -3, -1, 0, 1, 3, 5, 7], targetSum=-5) == [-5, 0]

def test_twoNumberSum_case_8():
    assert twoNumberSum(array=[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], targetSum=163) == [210, -47]

def test_twoNumberSum_case_9():
    assert twoNumberSum(array=[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], targetSum=164) == []

def test_twoNumberSum_case_10():
    assert twoNumberSum(array=[3, 5, -4, 8, 11, 1, -1, 6], targetSum=15) == []

def test_twoNumberSum_case_11():
    assert twoNumberSum(array=[14], targetSum=15) == []

def test_twoNumberSum_case_12():
    assert twoNumberSum(array=[15], targetSum=15) == []

