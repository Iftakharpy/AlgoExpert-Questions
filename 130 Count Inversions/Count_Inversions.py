######################################################################################
# Solution 1

# time: O(n^2) | space: O(1)
def countInversions(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                inversions += 1
    return inversions


######################################################################################
# Solution 2

# time O(nlogn) | space O(n) - n is len(array)
def countInversions(array):
    return countSubArrayInversions(array, 0, len(array))

def countSubArrayInversions(array, low, high):
    if (high-low)<=1:
        return 0
    mid = (low+high)//2
    left_inversions = countSubArrayInversions(array, low, mid)
    right_inversions = countSubArrayInversions(array, mid, high)
    merging_inversions = mergeSortAndCountInversions(array, low, mid, high)
    return left_inversions+right_inversions+merging_inversions

def mergeSortAndCountInversions(array, low, mid, high):
    sorted_sub_array = []
    inversions = 0
    left = low
    right = mid
    while left<mid and right<high:
        if array[right]<array[left]:
            inversions += mid-left
            sorted_sub_array.append(array[right])
            right+=1
        else:
            sorted_sub_array.append(array[left])
            left+=1
    
    sorted_sub_array += array[left:mid] + array[right:high]
    
    for idx, num in enumerate(sorted_sub_array):
        array[low+idx] = num
    return inversions
