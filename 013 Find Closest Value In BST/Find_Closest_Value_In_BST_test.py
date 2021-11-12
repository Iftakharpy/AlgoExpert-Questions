from Find_Closest_Value_In_BST import findClosestValueInBst

def test_findClosestValueInBst_case_1():
    assert findClosestValueInBst(target=12, tree={'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': '13', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}) == 13

def test_findClosestValueInBst_case_2():
    assert findClosestValueInBst(target=100, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 100

def test_findClosestValueInBst_case_3():
    assert findClosestValueInBst(target=208, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 208

def test_findClosestValueInBst_case_4():
    assert findClosestValueInBst(target=4500, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 4500

def test_findClosestValueInBst_case_5():
    assert findClosestValueInBst(target=4501, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 4500

def test_findClosestValueInBst_case_6():
    assert findClosestValueInBst(target=-70, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == -51

def test_findClosestValueInBst_case_7():
    assert findClosestValueInBst(target=2000, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 1001

def test_findClosestValueInBst_case_8():
    assert findClosestValueInBst(target=6, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 5

def test_findClosestValueInBst_case_9():
    assert findClosestValueInBst(target=30000, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 55000

def test_findClosestValueInBst_case_10():
    assert findClosestValueInBst(target=-1, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 1

def test_findClosestValueInBst_case_11():
    assert findClosestValueInBst(target=29751, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 55000

def test_findClosestValueInBst_case_12():
    assert findClosestValueInBst(target=29749, tree={'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}) == 4500
