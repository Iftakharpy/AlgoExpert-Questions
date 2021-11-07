from Binary_Search import binarySearch

def test_binarySearch_case_1():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=33) == 3

def test_binarySearch_case_2():
    assert binarySearch(array=[1, 5, 23, 111], target=111) == 3

def test_binarySearch_case_3():
    assert binarySearch(array=[1, 5, 23, 111], target=5) == 1

def test_binarySearch_case_4():
    assert binarySearch(array=[1, 5, 23, 111], target=35) == -1

def test_binarySearch_case_5():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=0) == 0

def test_binarySearch_case_6():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=1) == 1

def test_binarySearch_case_7():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=21) == 2

def test_binarySearch_case_8():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=45) == 4

def test_binarySearch_case_9():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=61) == 6

def test_binarySearch_case_10():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=71) == 7

def test_binarySearch_case_11():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=72) == 8

def test_binarySearch_case_12():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=73) == 9

def test_binarySearch_case_13():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=70) == -1

def test_binarySearch_case_14():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], target=355) == 10

def test_binarySearch_case_15():
    assert binarySearch(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], target=354) == -1

def test_binarySearch_case_16():
    assert binarySearch(array=[1, 5, 23, 111], target=120) == -1

def test_binarySearch_case_17():
    assert binarySearch(array=[5, 23, 111], target=3) == -1

