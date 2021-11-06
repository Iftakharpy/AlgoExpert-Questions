from Node_Depths import nodeDepths, BinaryTree


def findNode(nodes, id):
    if id==None:
        return None

    for node in nodes:
        if node["id"] == id:
            n = BinaryTree(node['value'])
            n.left = findNode(nodes, node['left'])
            n.right = findNode(nodes, node['right'])
            return n

def buildTree(tree):
    nodes = tree['nodes']
    head = tree['root']
    return findNode(nodes, head)



def test_nodeDepths_case_1():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}
	tree = buildTree(tree)
	res = 16
	assert nodeDepths(tree) == res

def test_nodeDepths_case_2():
	tree = {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}
	tree = buildTree(tree)
	res = 0
	assert nodeDepths(tree) == res

def test_nodeDepths_case_3():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}
	tree = buildTree(tree)
	res = 1
	assert nodeDepths(tree) == res

def test_nodeDepths_case_4():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}
	tree = buildTree(tree)
	res = 2
	assert nodeDepths(tree) == res

def test_nodeDepths_case_5():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}
	tree = buildTree(tree)
	res = 4
	assert nodeDepths(tree) == res

def test_nodeDepths_case_6():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}
	tree = buildTree(tree)
	res = 21
	assert nodeDepths(tree) == res

def test_nodeDepths_case_7():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': '8', 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': '9', 'value': 8}, {'id': '9', 'left': None, 'right': '10', 'value': 9}, {'id': '10', 'left': None, 'right': '11', 'value': 10}, {'id': '11', 'left': None, 'right': '12', 'value': 11}, {'id': '12', 'left': '13', 'right': None, 'value': 12}, {'id': '13', 'left': None, 'right': None, 'value': 13}], 'root': '1'}
	tree = buildTree(tree)
	res = 42
	assert nodeDepths(tree) == res

def test_nodeDepths_case_8():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': '10', 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': '11', 'value': 10}, {'id': '11', 'left': '12', 'right': '13', 'value': 11}, {'id': '12', 'left': '14', 'right': None, 'value': 12}, {'id': '13', 'left': '15', 'right': '16', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '16', 'left': None, 'right': None, 'value': 16}], 'root': '1'}
	tree = buildTree(tree)
	res = 51
	assert nodeDepths(tree) == res

def test_nodeDepths_case_9():
	tree = {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': '7', 'right': None, 'value': 6}, {'id': '7', 'left': '8', 'right': None, 'value': 7}, {'id': '8', 'left': '9', 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}
	tree = buildTree(tree)
	res = 36
	assert nodeDepths(tree) == res
