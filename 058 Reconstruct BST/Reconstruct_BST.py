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


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return None
