# Best
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


# Good
# time O(log(n)) - n is len(array)
# space O(log(n)) - here n is max call stack size
def binarySearchHelper(array, target, low, high):
    mid = (low+high)//2
    # Base cases
    if array[mid] == target:
        return mid
    if low>high:
        return -1
    
    # Recursive case
    if target>array[mid]:
        low = mid + 1
    else:
        high = mid - 1
    return binarySearchHelper(array, target, low, high)

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)
