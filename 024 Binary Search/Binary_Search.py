# time O(log(n))
# space O(1)
def binarySearch(array, target):
    low = 0
    high = len(array)-1
    while low<=high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        if target > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
