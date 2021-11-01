# Good
# time O(nlogn) + O(n) -> O(nlogn)
# space O(n) - where n is len(array)
def sortedSquaredArray(array):
    squared = []
    for num in array:
        squared.append(num**2)
    squared.sort()
    return squared


# Best
# time O(n)
# space O(n)
def sortedSquaredArray(array):
    result = [0]*len(array)
    idx = len(array)-1
    
    left_idx = 0
    right_idx = idx
    while left_idx<=right_idx:
        left = abs(array[left_idx])
        right = abs(array[right_idx])
        if left > right:
            result[idx] = left**2
            left_idx += 1
        else:
            result[idx] = right**2
            right_idx -= 1
        idx -= 1
    return result