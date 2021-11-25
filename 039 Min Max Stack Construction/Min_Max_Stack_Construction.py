class Node:
    def __init__(self, value, minValue=None, maxValue=None):
        self._value = value
        self._min = minValue if minValue is not None else value
        self._max = maxValue if maxValue is not None else value
        self._next = None

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    # time O(1) | space O(1)
    def __init__(self, value=None):
        self.head = None if value is None else Node(value, value, value)

    # time O(1) | space O(1)
    def peek(self):
        if self.head is None:
            return None
        return self.head._value

    # time O(1) | space O(1)
    def pop(self):
        value = self.head._value
        new_head = self.head._next
        del(self.head)
        self.head = new_head
        return value

    # time O(1) | space O(1)
    def push(self, number):
        if self.head is None:
            self.head = Node(number)
        else:
            new_min = min(number, self.head._min)
            new_max = max(number, self.head._max)
            node = Node(number, new_min, new_max)
            node._next = self.head
            self.head = node

    # time O(1) | space O(1)
    def getMin(self):
        if self.head is None:
            return None
        return self.head._min

    # time O(1) | space O(1)
    def getMax(self):
        if self.head is None:
            return None
        return self.head._max
