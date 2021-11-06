from Palindrome_Check import isPalindrome

def test_isPalindrome_case_1():
    assert isPalindrome(string='abcdcba') == True

def test_isPalindrome_case_2():
    assert isPalindrome(string='a') == True

def test_isPalindrome_case_3():
    assert isPalindrome(string='ab') == False

def test_isPalindrome_case_4():
    assert isPalindrome(string='aba') == True

def test_isPalindrome_case_5():
    assert isPalindrome(string='abb') == False

def test_isPalindrome_case_6():
    assert isPalindrome(string='abba') == True

def test_isPalindrome_case_7():
    assert isPalindrome(string='abcdefghhgfedcba') == True

def test_isPalindrome_case_8():
    assert isPalindrome(string='abcdefghihgfedcba') == True

def test_isPalindrome_case_9():
    assert isPalindrome(string='abcdefghihgfeddcba') == False

