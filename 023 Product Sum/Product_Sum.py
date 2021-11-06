# time O(n) - n is number of numbers in array including nested arrays
# space O(d) - d is max depth of arrays (call stack size)
def productSum(array, depth=1):
    sum = 0
    for item in array:
        if type(item) == list:
            sum += productSum(item, depth+1)
        else:
            sum += item
    sum *= depth
    return sum
