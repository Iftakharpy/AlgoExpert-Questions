# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# With helper
def findClosestValueInBst(tree, target):
    return closestHelper(tree, target, tree.value)

# Average time: O(log(n)) | Average space: O(n)
# Worst time: O(n) | Worst space: O(n)
def closestHelper(root, target, closest):
	if root is None or closest==target:
		return closest
	
	if abs(target-closest) > abs(target-root.value):
		closest = root.value
	if target < root.value:
		return closestHelper(root.left, target, closest)
	return closestHelper(root.right, target, closest)


# Without helper
# Average time: O(log(n)) | Average space: O(n)
# Worst time: O(n) | Worst space: O(n)
def findClosestValueInBst(tree, target, closest=None):
    if tree is None or target==closest:
        return closest
    if closest==None:
        closest = tree.value
    if abs(target-tree.value) < abs(target-closest):
        closest = tree.value
    
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    return findClosestValueInBst(tree.right, target, closest)
