from math import ceil


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


class MinHeap:
    # time: O(n)
    # space: O(1)
    # n is len(array)
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    @classmethod
    def _get_parent_idx(cls, child_node_idx):
        return ceil(child_node_idx/2)-1
    @classmethod
    def _get_left_child_idx(cls, parent_node_idx):
        return (parent_node_idx*2)+1
    @classmethod
    def _get_right_child_idx(cls, parent_node_idx):
        return (parent_node_idx*2)+2
    
    # # time: O(nlogn) | space: O(1)
    # def buildHeap(self, array):
    #     for i in range(len(array)):
    #         self.siftUp(array, i)
    #     return array

    # time: O(n) | space: O(1)
    def buildHeap(self, array):
        for i in range(len(array)-1, -1, -1):
            self.siftDown(array, i, len(array)-1)
        return array
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    # time: O(logn) | space: O(1)
    # n is len(heap)
    def siftDown(self, heap, parent_idx, max_idx=None):
        max_idx = max_idx if max_idx is not None else len(heap) - 1
        left_child_idx = self._get_left_child_idx(parent_idx)

        while left_child_idx<=max_idx:
            right_child_idx = self._get_right_child_idx(parent_idx)
            
            # get the smallest number idx
            if right_child_idx<=max_idx:
                small_idx = left_child_idx if heap[left_child_idx]['num']<heap[right_child_idx]['num'] else right_child_idx
            else:
                small_idx = left_child_idx

            # move parent down or return
            if heap[small_idx]['num'] < heap[parent_idx]['num']:
                swap(heap, small_idx, parent_idx)
                parent_idx = small_idx
                left_child_idx = self._get_left_child_idx(parent_idx)
            else:
                return

    # time: O(logn)
    # space: O(1)
    def siftUp(self, heap, idx):
        parent_idx = self._get_parent_idx(idx)
        while  parent_idx>=0 and heap[idx]['num']<heap[parent_idx]['num']:
            swap(heap, idx, parent_idx)
            idx = parent_idx
            parent_idx = self._get_parent_idx(idx)

    def peek(self):
        return self.heap[0] if self.heap else None

    # time: O(logn)
    # space: O(1)
    def remove(self):
        val = self.heap[0]
        last_num = self.heap.pop()
        if len(self.heap)>=1:
            self.heap[0] = last_num
        
        self.siftDown(self.heap, 0, len(self.heap)-1)
        return val
    
    # time: O(logn)
    # space: O(1)
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap)-1)
