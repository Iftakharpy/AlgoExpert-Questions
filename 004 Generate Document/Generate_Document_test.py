from Generate_Document import generateDocument

def test_generateDocument_case_1():
    assert generateDocument(characters='Bste!hetsi ogEAxpelrt x ', document='AlgoExpert is the Best!') == True

def test_generateDocument_case_2():
    assert generateDocument(characters='A', document='a') == False

def test_generateDocument_case_3():
    assert generateDocument(characters='a', document='a') == True

def test_generateDocument_case_4():
    assert generateDocument(characters='a hsgalhsa sanbjksbdkjba kjx', document='') == True

def test_generateDocument_case_5():
    assert generateDocument(characters=' ', document='hello') == False

def test_generateDocument_case_6():
    assert generateDocument(characters='     ', document='     ') == True

def test_generateDocument_case_7():
    assert generateDocument(characters='aheaollabbhb', document='hello') == True

def test_generateDocument_case_8():
    assert generateDocument(characters='aheaolabbhb', document='hello') == False

def test_generateDocument_case_9():
    assert generateDocument(characters='estssa', document='testing') == False

def test_generateDocument_case_10():
    assert generateDocument(characters='Bste!hetsi ogEAxpert', document='AlgoExpert is the Best!') == False

def test_generateDocument_case_11():
    assert generateDocument(characters='helloworld ', document='hello wOrld') == False

def test_generateDocument_case_12():
    assert generateDocument(characters='helloworldO', document='hello wOrld') == False

def test_generateDocument_case_13():
    assert generateDocument(characters='helloworldO ', document='hello wOrld') == True

def test_generateDocument_case_14():
    assert generateDocument(characters='&*&you^a%^&8766 _=-09     docanCMakemthisdocument', document='Can you make this document &') == True

def test_generateDocument_case_15():
    assert generateDocument(characters='abcabcabcacbcdaabc', document='bacaccadac') == True

