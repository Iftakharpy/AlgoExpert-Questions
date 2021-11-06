from Minimum_Waiting_Time import minimumWaitingTime

def test_minimumWaitingTime_case_1():
    assert minimumWaitingTime(queries=[3, 2, 1, 2, 6]) == 17

def test_minimumWaitingTime_case_2():
    assert minimumWaitingTime(queries=[2, 1, 1, 1]) == 6

def test_minimumWaitingTime_case_3():
    assert minimumWaitingTime(queries=[1, 2, 4, 5, 2, 1]) == 23

def test_minimumWaitingTime_case_4():
    assert minimumWaitingTime(queries=[25, 30, 2, 1]) == 32

def test_minimumWaitingTime_case_5():
    assert minimumWaitingTime(queries=[1, 1, 1, 1, 1]) == 10

def test_minimumWaitingTime_case_6():
    assert minimumWaitingTime(queries=[7, 9, 2, 3]) == 19

def test_minimumWaitingTime_case_7():
    assert minimumWaitingTime(queries=[4, 3, 1, 1, 3, 2, 1, 8]) == 45

def test_minimumWaitingTime_case_8():
    assert minimumWaitingTime(queries=[2]) == 0

def test_minimumWaitingTime_case_9():
    assert minimumWaitingTime(queries=[7]) == 0

def test_minimumWaitingTime_case_10():
    assert minimumWaitingTime(queries=[8, 9]) == 8

def test_minimumWaitingTime_case_11():
    assert minimumWaitingTime(queries=[1, 9]) == 1

def test_minimumWaitingTime_case_12():
    assert minimumWaitingTime(queries=[5, 4, 3, 2, 1]) == 20

def test_minimumWaitingTime_case_13():
    assert minimumWaitingTime(queries=[1, 2, 3, 4, 5]) == 20

def test_minimumWaitingTime_case_14():
    assert minimumWaitingTime(queries=[1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]) == 81

def test_minimumWaitingTime_case_15():
    assert minimumWaitingTime(queries=[17, 4, 3]) == 10

