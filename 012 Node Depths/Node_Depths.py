# time O(n) - n is the number of nodes
# space O(h) - h is max height of the tree
def nodeDepths(root, depth=0):
	if root==None:
		return depth
	
	left_depth = 0 if root.left is None else nodeDepths(root.left, depth+1)
	right_depth = 0 if root.right is None else nodeDepths(root.right, depth+1)
	
	return left_depth+right_depth + depth

# alternative
def nodeDepths(root, depth=0):
	if root==None:
		return 0
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
