# time O(n^2)
# space O(1)
def bubbleSort(array):
    for i in range(len(array)-1, 0, -1):
        is_swapped = False
        for j in range(i):
            if array[j] > array[j+1]:
                is_swapped=True
                array[j], array[j+1] = array[j+1], array[j]
        if not is_swapped:
            break
    return array
