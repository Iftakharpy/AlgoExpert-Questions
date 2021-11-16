from typing import List
from math import floor


def get_least_significent_digit(number:int, position=0, base=10)->int:
    return (number // base**position) % base

def get_counts(array:List[int], digit_column:int, base=10)->List[int]:
    counts = [0]*base
    for num in array:
        count_idx = get_least_significent_digit(num, digit_column, base)
        counts[count_idx] += 1
    for i in range(1, base):
        counts[i] += counts[i-1]
    return counts

def countSortByColumn(array, column, base):
    counts = get_counts(array, column, base)
    sorted_array = [0]*len(array)
    for idx in range(len(array)-1, -1, -1):
        digit = get_least_significent_digit(array[idx], column, base)
        counts[digit] -= 1
        sorted_idx = counts[digit]
        sorted_array[sorted_idx] = array[idx]
    return sorted_array

# time: O(d*(n+b))
# space: O(n+b)
def radixSort(array): # numbers in array are possitive
    base = 10
    max_num = max(array or [0])
    
    digit = 0
    while floor(max_num / base**digit) > 0:
        array = countSortByColumn(array, digit, base)
        digit += 1
    return array
