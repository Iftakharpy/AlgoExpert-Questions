# Worst solution
# time O(n^2) space O(1)
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		for j in range(len(array)):
			if i==j:
				continue
			if array[i]+array[j]==targetSum:
				return [array[i], array[j]]
	return []


# Good solution
# Time O(nlog(n))+O(n) -> O(nlog(n))
# Space O(1)
def twoNumberSum(array, targetSum):
	array.sort() # Time O(nlogn)
	
	left_idx = 0
	right_idx = len(array)-1
	while right_idx > left_idx: # time O(n)
		left = array[left_idx]
		right = array[right_idx]
		total = left+right
		if total == targetSum:
			return [left, right]
		elif total<targetSum:
			left_idx+=1
		else:
			right_idx-=1
	return []


# Best solution
# Space & time O(n)
def twoNumberSum(array, targetSum):
	seen_numbers = set()
	for number in array:
		compliment = targetSum-number
		if compliment in seen_numbers:
			return [compliment, number]
		else:
			seen_numbers.add(number)
	return []
