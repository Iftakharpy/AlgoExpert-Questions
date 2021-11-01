from Sorted_Squared_Array import sortedSquaredArray

def test_sortedSquaredArray_case_1():
    assert sortedSquaredArray(array=[1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81]

def test_sortedSquaredArray_case_2():
    assert sortedSquaredArray(array=[1]) == [1]

def test_sortedSquaredArray_case_3():
    assert sortedSquaredArray(array=[1, 2]) == [1, 4]

def test_sortedSquaredArray_case_4():
    assert sortedSquaredArray(array=[1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_sortedSquaredArray_case_5():
    assert sortedSquaredArray(array=[0]) == [0]

def test_sortedSquaredArray_case_6():
    assert sortedSquaredArray(array=[10]) == [100]

def test_sortedSquaredArray_case_7():
    assert sortedSquaredArray(array=[-1]) == [1]

def test_sortedSquaredArray_case_8():
    assert sortedSquaredArray(array=[-2, -1]) == [1, 4]

def test_sortedSquaredArray_case_9():
    assert sortedSquaredArray(array=[-5, -4, -3, -2, -1]) == [1, 4, 9, 16, 25]

def test_sortedSquaredArray_case_10():
    assert sortedSquaredArray(array=[-10]) == [100]

def test_sortedSquaredArray_case_11():
    assert sortedSquaredArray(array=[-10, -5, 0, 5, 10]) == [0, 25, 25, 100, 100]

def test_sortedSquaredArray_case_12():
    assert sortedSquaredArray(array=[-7, -3, 1, 9, 22, 30]) == [1, 9, 49, 81, 484, 900]

def test_sortedSquaredArray_case_13():
    assert sortedSquaredArray(array=[-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

def test_sortedSquaredArray_case_14():
    assert sortedSquaredArray(array=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_sortedSquaredArray_case_15():
    assert sortedSquaredArray(array=[-1, -1, 2, 3, 3, 3, 4]) == [1, 1, 4, 9, 9, 9, 16]

def test_sortedSquaredArray_case_16():
    assert sortedSquaredArray(array=[-3, -2, -1]) == [1, 4, 9]

def test_sortedSquaredArray_case_17():
    assert sortedSquaredArray(array=[-3, -2, -1]) == [1, 4, 9]

