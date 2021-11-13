from Three_Number_Sort import threeNumberSort

def test_threeNumberSort_case_1():
    assert threeNumberSort(array=[1, 0, 0, -1, -1, 0, 1, 1], order=[0, 1, -1]) == [0, 0, 0, 1, 1, 1, -1, -1]

def test_threeNumberSort_case_2():
    assert threeNumberSort(array=[7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], order=[8, 7, 9]) == [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]

def test_threeNumberSort_case_3():
    assert threeNumberSort(array=[], order=[0, 7, 9]) == []

def test_threeNumberSort_case_4():
    assert threeNumberSort(array=[-2, -3, -3, -3, -3, -3, -2, -2, -3], order=[-2, -3, 0]) == [-2, -2, -2, -3, -3, -3, -3, -3, -3]

def test_threeNumberSort_case_5():
    assert threeNumberSort(array=[0, 10, 10, 10, 10, 10, 25, 25, 25, 25, 25], order=[25, 10, 0]) == [25, 25, 25, 25, 25, 10, 10, 10, 10, 10, 0]

def test_threeNumberSort_case_6():
    assert threeNumberSort(array=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], order=[4, 5, 6]) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

def test_threeNumberSort_case_7():
    assert threeNumberSort(array=[1, 3, 4, 4, 4, 4, 3, 3, 3, 4, 1, 1, 1, 4, 4, 1, 3, 1, 4, 4], order=[1, 4, 3]) == [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]

def test_threeNumberSort_case_8():
    assert threeNumberSort(array=[1, 2, 3], order=[3, 1, 2]) == [3, 1, 2]

def test_threeNumberSort_case_9():
    assert threeNumberSort(array=[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2], order=[1, 2, 0]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0]

def test_threeNumberSort_case_10():
    assert threeNumberSort(array=[7, 7, 7, 11, 11, 7, 11, 7], order=[11, 7, 9]) == [11, 11, 11, 7, 7, 7, 7, 7]

def test_threeNumberSort_case_11():
    assert threeNumberSort(array=[9, 9, 9, 7, 9, 7, 9, 9, 7, 9], order=[11, 7, 9]) == [7, 7, 7, 9, 9, 9, 9, 9, 9, 9]

def test_threeNumberSort_case_12():
    assert threeNumberSort(array=[9, 9, 9, 7, 9, 7, 9, 9, 7, 9], order=[7, 11, 9]) == [7, 7, 7, 9, 9, 9, 9, 9, 9, 9]

def test_threeNumberSort_case_13():
    assert threeNumberSort(array=[1], order=[0, 1, 2]) == [1]

def test_threeNumberSort_case_14():
    assert threeNumberSort(array=[0, 1], order=[1, 2, 0]) == [1, 0]

