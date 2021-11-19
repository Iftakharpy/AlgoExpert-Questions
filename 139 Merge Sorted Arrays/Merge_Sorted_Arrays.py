##############################################################################################################
# Solution 1

# Time complexity is not a optimized
# time: O(m+n^2) | space: O(n)
# where n is the number of all numbers in the arrays and
# m is the number of arrays in arrays
def mergeSortedArrays(arrays):
    if len(arrays) == 1:
        return arrays[0]
    
    merged = arrays[0]
    for i in range(1,len(arrays)):
        array_one = arrays[i]
        merged = mergeTwoSortedArrays(array_one, merged)
        # The above line takses O(n^2 time).
        # We are storing the merged arrays in merged variable.
        # Which grows after calling mergeTwoSortedArrays function over time
        # when the next time we call mergeTwoSortedArrays passing merged array and array_one array,
        # the size of the array has become len(merged) + len(array_one)z
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


##############################################################################################################
# Solution 2

from minHeap import MinHeap


# O(nlog(k) + k) time | O(n + k) space - where n is the total
# number of array elements and k is the number of arrays
def mergeSortedArrays(arrays):
    sorted_list = []
    
    smallest_nums = []
    for idx in range(len(arrays)):
        smallest_nums.append({'arrayIdx': idx, 'elementIdx': 0, 'num': arrays[idx][0]})
    
    minHeap = MinHeap(smallest_nums)
    while not minHeap.isEmpty():
        smallest_item = minHeap.remove() # time: O(log(k))
        arrayIdx, elementIdx, num = map(smallest_item.get, ('arrayIdx', 'elementIdx', 'num'))
        sorted_list.append(num)
        if elementIdx >= len(arrays[arrayIdx])-1:
            continue
        elementIdx += 1
        minHeap.insert({'arrayIdx': arrayIdx, 'elementIdx': elementIdx, 'num': arrays[arrayIdx][elementIdx]})
    return sorted_list
