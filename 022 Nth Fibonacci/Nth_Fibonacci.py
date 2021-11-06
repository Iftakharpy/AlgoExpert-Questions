# Best
# time O(n)
# space O(1)
def getNthFib(n):
    first = 0
    second = 1
    res = first
    for i in range(n-1):
        res = first+second
        first = second
        second = res
        res = first
    return res

# Better
# time O(n)
# space O(n) - both callstack and memo uses n spaces
def getNthFib(n, memo={}):
    if n<=1:
        memo[n] = 0
        return memo[n]
    if n==2:
        memo[n] = 1
        return memo[n]
    if n in memo:
        return memo[n]
    memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)
    return memo[n]

# Worst
# time O(2^n)
# space O(n) - callstack uses n spaces
def getNthFib(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)
