def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def siftDown(array, idx, max_idx=None):
    if max_idx is None:
        max_idx = len(array) - 1
    left_child_idx = (2*idx) + 1
    while left_child_idx<=max_idx:
        right_child_idx = (2*idx) + 2
        if right_child_idx<=max_idx and array[right_child_idx] > array[left_child_idx]:
            swap_with_idx = right_child_idx
        else:
            swap_with_idx = left_child_idx
        if array[swap_with_idx] > array[idx]:
            swap(array, swap_with_idx, idx)
            idx = swap_with_idx
            left_child_idx = (2*idx) + 1
        else:
            return 

# time: O(n) | space: O(1)
def buildMaxHeap(array):
    # skip leaf nodes and build max heap
    first_parent_node_idx = len(array)//2
    # rearrange parent nodes
    for i in range(first_parent_node_idx-1, -1, -1):
        siftDown(array, i, max_idx=len(array)-1)


# time: O(n + nlogn) -> O(nlogn) | space O(1)
def heapSort(array):
    buildMaxHeap(array)
    for i in range(len(array)-1, 0, -1):
        swap(array, i, 0)
        siftDown(array, 0, i-1)
    return array
