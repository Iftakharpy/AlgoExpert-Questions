from Reconstruct_BST import reconstructBst, BST, reconstructBst


def findNode(nodes, id):
    if id==None:
        return None

    for node in nodes:
        if node["id"] == id:
            n = BST(node['value'])
            n.left = findNode(nodes, node['left'])
            n.right = findNode(nodes, node['right'])
            return n

def buildTree(tree):
    nodes = tree['nodes']
    head = tree['root']
    return findNode(nodes, head)

def test_reconstructBst_case_1():
    tree={'nodes': [{'id': '10', 'left': '4', 'right': '17', 'value': 10}, {'id': '17', 'left': None, 'right': '19', 'value': 17}, {'id': '19', 'left': '18', 'right': None, 'value': 19}, {'id': '18', 'left': None, 'right': None, 'value': 18}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[10, 4, 2, 1, 5, 17, 19, 18]) ==  tree

def test_reconstructBst_case_2():
    tree={'nodes': [{'id': '100', 'left': None, 'right': None, 'value': 100}], 'root': '100'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[100]) ==  tree

def test_reconstructBst_case_3():
    tree={'nodes': [{'id': '10', 'left': '9', 'right': None, 'value': 10}, {'id': '9', 'left': '8', 'right': None, 'value': 9}, {'id': '8', 'left': '7', 'right': None, 'value': 8}, {'id': '7', 'left': '6', 'right': None, 'value': 7}, {'id': '6', 'left': '5', 'right': None, 'value': 6}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '10'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[10, 9, 8, 7, 6, 5]) ==  tree

def test_reconstructBst_case_4():
    tree={'nodes': [{'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '5'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[5, 6, 7, 8]) ==  tree

def test_reconstructBst_case_5():
    tree={'nodes': [{'id': '5', 'left': '-10', 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': '7', 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '-10', 'left': None, 'right': '-5', 'value': -10}, {'id': '-5', 'left': None, 'right': None, 'value': -5}], 'root': '5'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[5, -10, -5, 6, 9, 7]) ==  tree

def test_reconstructBst_case_6():
    tree={'nodes': [{'id': '10', 'left': '4', 'right': '17', 'value': 10}, {'id': '17', 'left': None, 'right': '19', 'value': 17}, {'id': '19', 'left': '18', 'right': None, 'value': 19}, {'id': '18', 'left': None, 'right': None, 'value': 18}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': '7', 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[10, 4, 2, 1, 3, 5, 6, 9, 7, 17, 19, 18]) ==  tree

def test_reconstructBst_case_7():
    tree={'nodes': [{'id': '1', 'left': '0', 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '0', 'left': None, 'right': None, 'value': 0}], 'root': '1'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[1, 0, 2]) ==  tree

def test_reconstructBst_case_8():
    tree={'nodes': [{'id': '2', 'left': '0', 'right': None, 'value': 2}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[2, 0, 1]) ==  tree

def test_reconstructBst_case_9():
    tree={'nodes': [{'id': '2', 'left': '0', 'right': '4', 'value': 2}, {'id': '4', 'left': '3', 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[2, 0, 1, 4, 3]) ==  tree

def test_reconstructBst_case_10():
    tree={'nodes': [{'id': '2', 'left': '0', 'right': '4', 'value': 2}, {'id': '4', 'left': '3', 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': '3-2', 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[2, 0, 1, 4, 3, 3]) ==  tree

def test_reconstructBst_case_11():
    tree={'nodes': [{'id': '2', 'left': '0', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': '3-2', 'right': None, 'value': 4}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[2, 0, 1, 3, 4, 3]) ==  tree

def test_reconstructBst_case_12():
    tree={'nodes': [{'id': '10', 'left': '4', 'right': '17', 'value': 10}, {'id': '17', 'left': None, 'right': '19', 'value': 17}, {'id': '19', 'left': '18', 'right': '19-2', 'value': 19}, {'id': '19-2', 'left': None, 'right': None, 'value': 19}, {'id': '18', 'left': None, 'right': '18-2', 'value': 18}, {'id': '18-2', 'left': None, 'right': None, 'value': 18}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': '5-3', 'right': '9', 'value': 6}, {'id': '9', 'left': '7', 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '5-3', 'left': None, 'right': '5-4', 'value': 5}, {'id': '5-4', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}
    tree=buildTree(tree)
    assert reconstructBst(preOrderTraversalValues=[10, 4, 2, 1, 3, 5, 5, 6, 5, 5, 9, 7, 17, 19, 18, 18, 19]) ==  tree
