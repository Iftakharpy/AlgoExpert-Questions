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
