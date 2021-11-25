# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # time O(1) | space O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # time O(1) | space O(1)
    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    # time O(1) | space O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # time O(1) | space O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # time O(p) | space O(1) - p is position
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition < position:
            node = node.next
            currentPosition += 1
        if node is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)
    
    # time O(1) | space O(1)
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    # time O(n) | space O(1) - n is length of the linked list
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value==value:
                self.remove(nodeToRemove)

    # time O(1) | space O(1)
    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # time O(n) | space O(1) - n is length of the linked list
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value!=value:
            node = node.next
        return node is not None
