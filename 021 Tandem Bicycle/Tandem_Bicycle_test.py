from Tandem_Bicycle import tandemBicycle

def test_tandemBicycle_case_1():
    assert tandemBicycle(blueShirtSpeeds=[3, 6, 7, 2, 1], fastest=True, redShirtSpeeds=[5, 5, 3, 9, 2]) == 32

def test_tandemBicycle_case_2():
    assert tandemBicycle(blueShirtSpeeds=[3, 6, 7, 2, 1], fastest=False, redShirtSpeeds=[5, 5, 3, 9, 2]) == 25

def test_tandemBicycle_case_3():
    assert tandemBicycle(blueShirtSpeeds=[3, 3, 4, 6, 1, 2], fastest=False, redShirtSpeeds=[1, 2, 1, 9, 12, 3]) == 30

def test_tandemBicycle_case_4():
    assert tandemBicycle(blueShirtSpeeds=[3, 3, 4, 6, 1, 2], fastest=True, redShirtSpeeds=[1, 2, 1, 9, 12, 3]) == 37

def test_tandemBicycle_case_5():
    assert tandemBicycle(blueShirtSpeeds=[3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], fastest=True, redShirtSpeeds=[1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]) == 816

def test_tandemBicycle_case_6():
    assert tandemBicycle(blueShirtSpeeds=[3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], fastest=False, redShirtSpeeds=[1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]) == 484

def test_tandemBicycle_case_7():
    assert tandemBicycle(blueShirtSpeeds=[5], fastest=True, redShirtSpeeds=[1]) == 5

def test_tandemBicycle_case_8():
    assert tandemBicycle(blueShirtSpeeds=[5], fastest=False, redShirtSpeeds=[1]) == 5

def test_tandemBicycle_case_9():
    assert tandemBicycle(blueShirtSpeeds=[1, 1, 1, 1], fastest=True, redShirtSpeeds=[1, 1, 1, 1]) == 4

def test_tandemBicycle_case_10():
    assert tandemBicycle(blueShirtSpeeds=[1, 1, 1, 1], fastest=False, redShirtSpeeds=[1, 1, 1, 1]) == 4

def test_tandemBicycle_case_11():
    assert tandemBicycle(blueShirtSpeeds=[1, 1, 1, 1, 3, 3, 3, 3, 5, 7], fastest=True, redShirtSpeeds=[1, 1, 1, 1, 2, 2, 2, 2, 9, 11]) == 48

def test_tandemBicycle_case_12():
    assert tandemBicycle(blueShirtSpeeds=[1, 1, 1, 1, 3, 3, 3, 3, 5, 7], fastest=False, redShirtSpeeds=[1, 1, 1, 1, 2, 2, 2, 2, 9, 11]) == 36

def test_tandemBicycle_case_13():
    assert tandemBicycle(blueShirtSpeeds=[3, 4, 4, 1, 1, 8, 9], fastest=True, redShirtSpeeds=[9, 8, 2, 2, 3, 5, 6]) == 49

def test_tandemBicycle_case_14():
    assert tandemBicycle(blueShirtSpeeds=[3, 4, 4, 1, 1, 8, 9], fastest=False, redShirtSpeeds=[9, 8, 2, 2, 3, 5, 6]) == 35

def test_tandemBicycle_case_15():
    assert tandemBicycle(blueShirtSpeeds=[1, 2, 3, 4, 5], fastest=False, redShirtSpeeds=[5, 4, 3, 2, 1]) == 15

def test_tandemBicycle_case_16():
    assert tandemBicycle(blueShirtSpeeds=[1, 2, 3, 4, 5], fastest=True, redShirtSpeeds=[5, 4, 3, 2, 1]) == 21

def test_tandemBicycle_case_17():
    assert tandemBicycle(blueShirtSpeeds=[], fastest=True, redShirtSpeeds=[]) == 0

