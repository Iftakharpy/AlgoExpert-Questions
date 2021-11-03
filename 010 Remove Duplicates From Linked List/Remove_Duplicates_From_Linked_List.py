# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Node(value={self.value}, next={self.next})"
    
    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)



# time O(n)
# space O(1)
def removeDuplicatesFromLinkedList(linkedList):
    if not linkedList:
        return None
    
    head = linkedList
    while head:
        if head.next!=None and head.value==head.next.value:
            head.next = head.next.next
        else:
            head=head.next
    return linkedList
