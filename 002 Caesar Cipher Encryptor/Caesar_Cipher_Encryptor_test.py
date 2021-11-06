from Caesar_Cipher_Encryptor import caesarCipherEncryptor

def test_caesarCipherEncryptor_case_1():
    assert caesarCipherEncryptor(key=2, string='xyz') == 'zab'

def test_caesarCipherEncryptor_case_2():
    assert caesarCipherEncryptor(key=0, string='abc') == 'abc'

def test_caesarCipherEncryptor_case_3():
    assert caesarCipherEncryptor(key=3, string='abc') == 'def'

def test_caesarCipherEncryptor_case_4():
    assert caesarCipherEncryptor(key=5, string='xyz') == 'cde'

def test_caesarCipherEncryptor_case_5():
    assert caesarCipherEncryptor(key=26, string='abc') == 'abc'

def test_caesarCipherEncryptor_case_6():
    assert caesarCipherEncryptor(key=52, string='abc') == 'abc'

def test_caesarCipherEncryptor_case_7():
    assert caesarCipherEncryptor(key=57, string='abc') == 'fgh'

def test_caesarCipherEncryptor_case_8():
    assert caesarCipherEncryptor(key=25, string='xyz') == 'wxy'

def test_caesarCipherEncryptor_case_9():
    assert caesarCipherEncryptor(key=25, string='iwufqnkqkqoolxzzlzihqfm') == 'hvtepmjpjpnnkwyykyhgpel'

def test_caesarCipherEncryptor_case_10():
    assert caesarCipherEncryptor(key=52, string='ovmqkwtujqmfkao') == 'ovmqkwtujqmfkao'

def test_caesarCipherEncryptor_case_11():
    assert caesarCipherEncryptor(key=7, string='mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf') == 'tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm'

def test_caesarCipherEncryptor_case_12():
    assert caesarCipherEncryptor(key=15, string='kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh') == 'zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw'

