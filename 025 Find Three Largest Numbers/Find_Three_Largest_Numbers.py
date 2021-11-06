from math import inf

# time O(n)
# space O(1)
def findThreeLargestNumbers(array):
    res = [-inf, -inf, -inf]
    for num in array:
        if num >= res[2]:
            res.append(num)
            res.pop(0)
        elif num >= res[1]:
            res.insert(2, num)
            res.pop(0)
        elif num > res[0]:
            res[0] = num
    return res
