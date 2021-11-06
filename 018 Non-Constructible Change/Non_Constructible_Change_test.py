from Non_Constructible_Change import nonConstructibleChange

def test_nonConstructibleChange_case_1():
    assert nonConstructibleChange(coins=[5, 7, 1, 1, 2, 3, 22]) == 20

def test_nonConstructibleChange_case_2():
    assert nonConstructibleChange(coins=[1, 1, 1, 1, 1]) == 6

def test_nonConstructibleChange_case_3():
    assert nonConstructibleChange(coins=[1, 5, 1, 1, 1, 10, 15, 20, 100]) == 55

def test_nonConstructibleChange_case_4():
    assert nonConstructibleChange(coins=[6, 4, 5, 1, 1, 8, 9]) == 3

def test_nonConstructibleChange_case_5():
    assert nonConstructibleChange(coins=[]) == 1

def test_nonConstructibleChange_case_6():
    assert nonConstructibleChange(coins=[87]) == 1

def test_nonConstructibleChange_case_7():
    assert nonConstructibleChange(coins=[5, 6, 1, 1, 2, 3, 4, 9]) == 32

def test_nonConstructibleChange_case_8():
    assert nonConstructibleChange(coins=[5, 6, 1, 1, 2, 3, 43]) == 19

def test_nonConstructibleChange_case_9():
    assert nonConstructibleChange(coins=[1, 1]) == 3

def test_nonConstructibleChange_case_10():
    assert nonConstructibleChange(coins=[2]) == 1

def test_nonConstructibleChange_case_11():
    assert nonConstructibleChange(coins=[1]) == 2

def test_nonConstructibleChange_case_12():
    assert nonConstructibleChange(coins=[109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]) == 87

def test_nonConstructibleChange_case_13():
    assert nonConstructibleChange(coins=[1, 2, 3, 4, 5, 6, 7]) == 29

