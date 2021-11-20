from Count_Inversions import countInversions

def test_countInversions_case_1():
    assert countInversions(array=[2, 3, 3, 1, 9, 5, 6]) == 5

def test_countInversions_case_2():
    assert countInversions(array=[]) == 0

def test_countInversions_case_3():
    assert countInversions(array=[1, 2, 3, 4, 5, 6, -1]) == 6

def test_countInversions_case_4():
    assert countInversions(array=[0, 2, 4, 5, 76]) == 0

def test_countInversions_case_5():
    assert countInversions(array=[54, 1, 2, 3, 4]) == 4

def test_countInversions_case_6():
    assert countInversions(array=[1, 10, 2, 8, 3, 7, 4, 6, 5]) == 16

def test_countInversions_case_7():
    assert countInversions(array=[2, -18]) == 1

def test_countInversions_case_8():
    assert countInversions(array=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105

def test_countInversions_case_9():
    assert countInversions(array=[5, -1, 2, -4, 3, 4, 19, 87, 762, -8, 0]) == 23

def test_countInversions_case_10():
    assert countInversions(array=[1, 1, 1, 1, 1, 1, 1, 1]) == 0

def test_countInversions_case_11():
    assert countInversions(array=[1, 1, 1, 1, 0, 1, 1, 1]) == 4

def test_countInversions_case_12():
    assert countInversions(array=[2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3]) == 16

def test_countInversions_case_13():
    assert countInversions(array=[3, 1, 2]) == 2

def test_countInversions_case_14():
    assert countInversions(array=[3, 2, 1, 1]) == 5

def test_countInversions_case_15():
    assert countInversions(array=[10, 7, 2, 3, 1, -9, -86, -862, 234, 312, 3421, 23, 0, 2, 1, 2]) == 62

