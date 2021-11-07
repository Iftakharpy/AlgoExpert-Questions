# time O(n^2)
# space O(1)
def selectionSort(array):
    for swap_with in range(len(array)-1):
        smallest = swap_with
        for finder in range(swap_with, len(array)):
            if array[finder] < array[smallest]:
                smallest = finder
        array[swap_with], array[smallest] = array[smallest], array[swap_with]
    return array
