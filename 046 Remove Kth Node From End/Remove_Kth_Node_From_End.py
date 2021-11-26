class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(n) | space O(1)
def removeKthNodeFromEnd(head, k):
    endFinder = head
    for i in range(k):
        endFinder = endFinder.next
    
    if endFinder is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    
    node = head
    while endFinder.next is not None:
        node = node.next
        endFinder = endFinder.next
    
    node.next = node.next.next
