# time: O(m+n)
# space: O(n)
# where n is the number of all numbers in the arrays and
# m is the number of arrays in arrays
def mergeSortedArrays(arrays):
    if len(arrays) == 1:
        return arrays[0]
    
    merged = arrays[0]
    for i in range(1,len(arrays)):
        array_one = arrays[i]
        merged = mergeTwoSortedArrays(array_one, merged)
    return merged

# time and space complexity: O(m+n) 
# m is len(array_one) and n is len(array_two)
def mergeTwoSortedArrays(array_one, array_two):
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
