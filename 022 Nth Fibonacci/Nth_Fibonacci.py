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
