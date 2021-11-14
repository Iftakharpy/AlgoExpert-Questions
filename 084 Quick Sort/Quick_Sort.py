def swap(array:list, i:int, j:int) -> None:
    array[i], array[j] = array[j], array[i]

def shuffle(array:list, low_idx:int, high_idx:int, pivot_idx:int) -> int:
    """Takes an array, low index, high index and a pivot index puts.
    And puts the number at the pivot index at the correct index().
    Then returns the correct index for the number.
    """
    while low_idx<=high_idx:
        if array[low_idx] <= array[pivot_idx]:
            low_idx+=1
        elif array[high_idx] > array[pivot_idx]:
            high_idx-=1
        else:
            swap(array, low_idx, high_idx)
    swap(array, pivot_idx, high_idx)
    return high_idx

def quickSortHelper(array:list, low:int, high:int) -> None:
    if low>=high or low<0 or high>len(array)-1:
        return
    pivot = shuffle(array, low+1, high, low)
    quickSortHelper(array, low, pivot-1)
    quickSortHelper(array, pivot+1, high)

def quickSort(array:list) -> list:
    quickSortHelper(array, 0, len(array)-1)
    return array
