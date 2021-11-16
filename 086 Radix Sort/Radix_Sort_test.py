from Radix_Sort import radixSort

def test_radixSort_case_1():
    assert radixSort(array=[8762, 654, 3008, 345, 87, 65, 234, 12, 2]) == [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

def test_radixSort_case_2():
    assert radixSort(array=[2, 12, 65, 87, 234, 345, 654, 3008, 8762]) == [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

def test_radixSort_case_3():
    assert radixSort(array=[111, 11, 11, 1, 0]) == [0, 1, 11, 11, 111]

def test_radixSort_case_4():
    assert radixSort(array=[12, 123, 456, 986, 2, 3, 34, 543, 97654, 34200]) == [2, 3, 12, 34, 123, 456, 543, 986, 34200, 97654]

def test_radixSort_case_5():
    assert radixSort(array=[4, 44, 444, 888, 88, 33, 3, 22, 2222, 1111, 1234]) == [3, 4, 22, 33, 44, 88, 444, 888, 1111, 1234, 2222]

def test_radixSort_case_6():
    assert radixSort(array=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_radixSort_case_7():
    assert radixSort(array=[]) == []

def test_radixSort_case_8():
    assert radixSort(array=[100]) == [100]

def test_radixSort_case_9():
    assert radixSort(array=[10000, 100001, 10001, 10101, 101, 11, 100, 10, 1, 0]) == [0, 1, 10, 11, 100, 101, 10000, 10001, 10101, 100001]

def test_radixSort_case_10():
    assert radixSort(array=[34, 56, 7373, 2321, 3421, 8272, 232, 23892831, 230983, 2312, 7878, 87, 234, 23, 332, 4556]) == [23, 34, 56, 87, 232, 234, 332, 2312, 2321, 3421, 4556, 7373, 7878, 8272, 230983, 23892831]

def test_radixSort_case_11():
    assert radixSort(array=[10, 87, 2321, 3221, 2312, 7632, 6542, 3223, 231, 2342, 321, 9, 1, 323, 421, 325, 65, 789, 4002]) == [1, 9, 10, 65, 87, 231, 321, 323, 325, 421, 789, 2312, 2321, 2342, 3221, 3223, 4002, 6542, 7632]

def test_radixSort_case_12():
    assert radixSort(array=[0, 1, 2, 22, 11, 3, 33, 0, 0, 0, 21, 21, 21, 1, 11, 111]) == [0, 0, 0, 0, 1, 1, 2, 3, 11, 11, 21, 21, 21, 22, 33, 111]

def test_radixSort_case_13():
    assert radixSort(array=[8, 4, 5, 34, 234, 987, 444, 23, 21, 8, 1, 0]) == [0, 1, 4, 5, 8, 8, 21, 23, 34, 234, 444, 987]

def test_radixSort_case_14():
    assert radixSort(array=[1, 11]) == [1, 11]

def test_radixSort_case_15():
    assert radixSort(array=[1, 11, 1, 11, 101, 9, 99, 432, 441]) == [1, 1, 9, 11, 11, 99, 101, 432, 441]

def test_radixSort_case_16():
    assert radixSort(array=[1000, 100, 10, 1, 10, 100, 1000, 10001, 10201, 1001, 0, 1, 1]) == [0, 1, 1, 1, 10, 10, 100, 100, 1000, 1000, 1001, 10001, 10201]

def test_radixSort_case_17():
    assert radixSort(array=[9, 109, 908, 876, 1099, 190, 290, 999, 9999]) == [9, 109, 190, 290, 876, 908, 999, 1099, 9999]

def test_radixSort_case_18():
    assert radixSort(array=[0, 999999, 234892, 10000009, 89892, 782731, 891932, 92012, 1892193, 181730, 785239, 2314451, 1231421, 812723]) == [0, 89892, 92012, 181730, 234892, 782731, 785239, 812723, 891932, 999999, 1231421, 1892193, 2314451, 10000009]

