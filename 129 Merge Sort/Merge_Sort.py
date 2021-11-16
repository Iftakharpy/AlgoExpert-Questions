# Worst, Average, Best time and space compelexity O(nlogn)
def mergeSort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return mergeSortedArrays(left, right)


def mergeSortedArrays(array_one, array_two):
    merged = []
    
    idx_one = 0
    idx_two = 0
    while idx_one<len(array_one) and idx_two<len(array_two):
        if array_one[idx_one] < array_two[idx_two]:
            merged.append(array_one[idx_one])
            idx_one += 1
        else:
            merged.append(array_two[idx_two])
            idx_two += 1
    
    while idx_one<len(array_one):
        merged.append(array_one[idx_one])
        idx_one+=1
    while idx_two<len(array_two):
        merged.append(array_two[idx_two])
        idx_two+=1
        
    return merged
