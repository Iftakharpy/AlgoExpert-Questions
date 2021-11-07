# time O(n^2)
# space O(1)
def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            unsorted_first = j
            sorted_last = j-1
            if array[unsorted_first]<array[sorted_last]:
                # Swap
                array[unsorted_first], array[sorted_last] = array[sorted_last], array[unsorted_first]
            else:
                break
    return array