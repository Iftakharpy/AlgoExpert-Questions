from Run_Length_Encoding import runLengthEncoding

def test_runLengthEncoding_case_1():
    assert runLengthEncoding(string='AAAAAAAAAAAAABBCCCCDD') == '9A4A2B4C2D'

def test_runLengthEncoding_case_2():
    assert runLengthEncoding(string='aA') == '1a1A'

def test_runLengthEncoding_case_3():
    assert runLengthEncoding(string='122333') == '112233'

def test_runLengthEncoding_case_4():
    assert runLengthEncoding(string='************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA') == '9*3*7^6$7%6!9A9A2A'

def test_runLengthEncoding_case_5():
    assert runLengthEncoding(string='aAaAaaaaaAaaaAAAABbbbBBBB') == '1a1A1a1A5a1A3a4A1B3b4B'

def test_runLengthEncoding_case_6():
    assert runLengthEncoding(string='                          ') == '9 9 8 '

def test_runLengthEncoding_case_7():
    assert runLengthEncoding(string='1  222 333    444  555') == '112 321 334 342 35'

def test_runLengthEncoding_case_8():
    assert runLengthEncoding(string='1A2BB3CCC4DDDD') == '111A122B133C144D'

def test_runLengthEncoding_case_9():
    assert runLengthEncoding(string='........______=========AAAA   AAABBBB   BBB') == '8.6_9=4A3 3A4B3 3B'

def test_runLengthEncoding_case_10():
    assert runLengthEncoding(string='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == '9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a1a'

def test_runLengthEncoding_case_11():
    assert runLengthEncoding(string='        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == '8 9a9a9a9a9a4a'

def test_runLengthEncoding_case_12():
    assert runLengthEncoding(string=' ') == '1 '

def test_runLengthEncoding_case_13():
    assert runLengthEncoding(string='[(aaaaaaa,bbbbbbb,ccccc,dddddd)]') == '1[1(7a1,7b1,5c1,6d1)1]'

def test_runLengthEncoding_case_14():
    assert runLengthEncoding(string=";;;;;;;;;;;;''''''''''''''''''''1233333332222211112222111s") == "9;3;9'9'2'111273524142311s"

def test_runLengthEncoding_case_15():
    assert runLengthEncoding(string='AAAAAAAAAAAAABBCCCCDDDDDDDDDDD') == '9A4A2B4C9D2D'

