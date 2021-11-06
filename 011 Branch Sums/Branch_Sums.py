# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# time O(n)
# space O(n)
# n is the number of nodes in the BinaryTree
def recSums(root, sums, sum=0):
	if root==None:
		return
	if root.left is not None:
		recSums(root.left, sums, sum=sum+root.value)
	if root.right is not None:
		recSums(root.right, sums, sum=sum+root.value)
	if root.left is None and root.right is None:
		sums.append(sum+root.value)
	return sums

def branchSums(root):
	sums = []
	recSums(root, sums, 0)
	return sums
