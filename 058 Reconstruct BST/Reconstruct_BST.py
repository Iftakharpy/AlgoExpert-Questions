from math import inf

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"BST(value={self.value}, left={self.left}, right={self.right})"
    
    def __eq__(self, __o: object) -> bool:
        return str(self) == str(__o)


############################################################################
# Solution 1

# time O(n^2) | space O(n+d) - n nodes and d call stack size
# n is len(preOrderTraversalValues)
# d is max depth of bst
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues)==0:
        return None
    bst = BST(preOrderTraversalValues[0])
    for i in range(1, len(preOrderTraversalValues)):
        insertIntoBST(bst, BST(preOrderTraversalValues[i]))
    return bst

# time O(n) | space O(n) - call stack space
# where n is the height of the BST
def insertIntoBST(bst, node):
    if node.value<bst.value:
        if bst.left is not None:
            insertIntoBST(bst.left, node)
        else:
            bst.left = node
    else:
        if bst.right is not None:
            insertIntoBST(bst.right, node)
        else:
            bst.right = node


############################################################################
# Solution 2

# Time O(n) | Space O(n)
def reconstructBst(preOrderTraversalValues):
    treeInfo = {'root_idx': 0} # using dict to make the root_idx global
    return reconstructBstFromRange(-inf, inf, preOrderTraversalValues, treeInfo)

# Time: O(n) | Space: O(n+h) - n BST nodes and h call stack size
# Where n is len(preOrderTraversalValues) and h is max heigh of BST.
def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues:list, currentSubtreeInfo:dict):
    curr_idx = currentSubtreeInfo['root_idx']
    if curr_idx>=len(preOrderTraversalValues):
        # Base case when preOrderTraversalValues are exausted
        return None
    
    rootValue = preOrderTraversalValues[curr_idx]
    if rootValue<lowerBound or rootValue>=upperBound:
        # Base case when node doesn't belong to current subtree
        return None
    
    currentSubtreeInfo['root_idx'] += 1
    # Build left subtree
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    # Build right subtree
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree) # Build tree
