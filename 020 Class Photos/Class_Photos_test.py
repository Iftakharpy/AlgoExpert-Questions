from Class_Photos import classPhotos

def test_classPhotos_case_1():
    assert classPhotos(blueShirtHeights=[6, 9, 2, 4, 5], redShirtHeights=[5, 8, 1, 3, 4]) == True

def test_classPhotos_case_2():
    assert classPhotos(blueShirtHeights=[5, 8, 1, 3, 4], redShirtHeights=[6, 9, 2, 4, 5]) == True

def test_classPhotos_case_3():
    assert classPhotos(blueShirtHeights=[5, 8, 1, 3, 4, 9], redShirtHeights=[6, 9, 2, 4, 5, 1]) == False

def test_classPhotos_case_4():
    assert classPhotos(blueShirtHeights=[6], redShirtHeights=[6]) == False

def test_classPhotos_case_5():
    assert classPhotos(blueShirtHeights=[125], redShirtHeights=[126]) == True

def test_classPhotos_case_6():
    assert classPhotos(blueShirtHeights=[2, 3, 4, 5, 6], redShirtHeights=[1, 2, 3, 4, 5]) == True

def test_classPhotos_case_7():
    assert classPhotos(blueShirtHeights=[5, 6, 7, 2, 3, 1, 2, 3], redShirtHeights=[1, 1, 1, 1, 1, 1, 1, 1]) == False

def test_classPhotos_case_8():
    assert classPhotos(blueShirtHeights=[2, 2, 2, 2, 2, 2, 2, 2], redShirtHeights=[1, 1, 1, 1, 1, 1, 1, 1]) == True

def test_classPhotos_case_9():
    assert classPhotos(blueShirtHeights=[126], redShirtHeights=[125]) == True

def test_classPhotos_case_10():
    assert classPhotos(blueShirtHeights=[21, 5, 4, 4, 4, 4, 4, 4, 4], redShirtHeights=[19, 2, 4, 6, 2, 3, 1, 1, 4]) == False

def test_classPhotos_case_11():
    assert classPhotos(blueShirtHeights=[20, 5, 4, 4, 4, 4, 4, 4], redShirtHeights=[19, 19, 21, 1, 1, 1, 1, 1]) == False

def test_classPhotos_case_12():
    assert classPhotos(blueShirtHeights=[2, 4, 7, 5, 1], redShirtHeights=[3, 5, 6, 8, 2]) == True

def test_classPhotos_case_13():
    assert classPhotos(blueShirtHeights=[2, 4, 7, 5, 1, 6], redShirtHeights=[3, 5, 6, 8, 2, 1]) == False

def test_classPhotos_case_14():
    assert classPhotos(blueShirtHeights=[5, 4], redShirtHeights=[4, 5]) == False

def test_classPhotos_case_15():
    assert classPhotos(blueShirtHeights=[5, 4], redShirtHeights=[5, 6]) == True

