from Product_Sum import productSum

def test_productSum_case_1():
    assert productSum(array=[5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12

def test_productSum_case_2():
    assert productSum(array=[1, 2, 3, 4, 5]) == 15

def test_productSum_case_3():
    assert productSum(array=[1, 2, [3], 4, 5]) == 18

def test_productSum_case_4():
    assert productSum(array=[[1, 2], 3, [4, 5]]) == 27

def test_productSum_case_5():
    assert productSum(array=[[[[[5]]]]]) == 600

def test_productSum_case_6():
    assert productSum(array=[9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]) == 1351

