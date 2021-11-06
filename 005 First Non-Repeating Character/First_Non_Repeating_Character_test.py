from First_Non_Repeating_Character import firstNonRepeatingCharacter

def test_firstNonRepeatingCharacter_case_1():
    assert firstNonRepeatingCharacter(string='abcdcaf') == 1

def test_firstNonRepeatingCharacter_case_2():
    assert firstNonRepeatingCharacter(string='faadabcbbebdf') == 6

def test_firstNonRepeatingCharacter_case_3():
    assert firstNonRepeatingCharacter(string='a') == 0

def test_firstNonRepeatingCharacter_case_4():
    assert firstNonRepeatingCharacter(string='ab') == 0

def test_firstNonRepeatingCharacter_case_5():
    assert firstNonRepeatingCharacter(string='abc') == 0

def test_firstNonRepeatingCharacter_case_6():
    assert firstNonRepeatingCharacter(string='abac') == 1

def test_firstNonRepeatingCharacter_case_7():
    assert firstNonRepeatingCharacter(string='ababac') == 5

def test_firstNonRepeatingCharacter_case_8():
    assert firstNonRepeatingCharacter(string='ababacc') == -1

def test_firstNonRepeatingCharacter_case_9():
    assert firstNonRepeatingCharacter(string='lmnopqldsafmnopqsa') == 7

def test_firstNonRepeatingCharacter_case_10():
    assert firstNonRepeatingCharacter(string='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy') == 25

def test_firstNonRepeatingCharacter_case_11():
    assert firstNonRepeatingCharacter(string='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz') == -1

def test_firstNonRepeatingCharacter_case_12():
    assert firstNonRepeatingCharacter(string='') == -1

def test_firstNonRepeatingCharacter_case_13():
    assert firstNonRepeatingCharacter(string='ggyllaylacrhdzedddjsc') == 10

def test_firstNonRepeatingCharacter_case_14():
    assert firstNonRepeatingCharacter(string='aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccdddddddddddeeeeeeeeffghgh') == -1

def test_firstNonRepeatingCharacter_case_15():
    assert firstNonRepeatingCharacter(string='aabbccddeeff') == -1

