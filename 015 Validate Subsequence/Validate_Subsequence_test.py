from Validate_Subsequence import isValidSubsequence

def test_isValidSubsequence_case_1():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, 10]) == True

def test_isValidSubsequence_case_2():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 25, 6, -1, 8, 10]) == True

def test_isValidSubsequence_case_3():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 6, -1, 8, 10]) == True

def test_isValidSubsequence_case_4():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[22, 25, 6]) == True

def test_isValidSubsequence_case_5():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, 10]) == True

def test_isValidSubsequence_case_6():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 10]) == True

def test_isValidSubsequence_case_7():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, -1, 8, 10]) == True

def test_isValidSubsequence_case_8():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[25]) == True

def test_isValidSubsequence_case_9():
    assert isValidSubsequence(array=[1, 1, 1, 1, 1], sequence=[1, 1, 1]) == True

def test_isValidSubsequence_case_10():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 25, 6, -1, 8, 10, 12]) == False

def test_isValidSubsequence_case_11():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[4, 5, 1, 22, 25, 6, -1, 8, 10]) == False

def test_isValidSubsequence_case_12():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 23, 6, -1, 8, 10]) == False

def test_isValidSubsequence_case_13():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 22, 25, 6, -1, 8, 10]) == False

def test_isValidSubsequence_case_14():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 22, 6, -1, 8, 10]) == False

def test_isValidSubsequence_case_15():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, -1]) == False

def test_isValidSubsequence_case_16():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, -1, 10]) == False

def test_isValidSubsequence_case_17():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, -2]) == False

def test_isValidSubsequence_case_18():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[26]) == False

def test_isValidSubsequence_case_19():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 25, 22, 6, -1, 8, 10]) == False

def test_isValidSubsequence_case_20():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 26, 22, 8]) == False

def test_isValidSubsequence_case_21():
    assert isValidSubsequence(array=[1, 1, 6, 1], sequence=[1, 1, 1, 6]) == False

def test_isValidSubsequence_case_22():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, 10, 11, 11, 11, 11]) == False

def test_isValidSubsequence_case_23():
    assert isValidSubsequence(array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[5, 1, 22, 25, 6, -1, 8, 10, 10]) == False

