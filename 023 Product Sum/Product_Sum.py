# time O(n) - n is the number of elements in array and their sub arrays.
# 			  Ex: [1, 2, [[[3]], [4]]] - O(8)
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
