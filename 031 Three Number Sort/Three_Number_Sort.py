# Eventhough I am using nested for loop time complexity here isn't O(n^2).
# Because the order array has at most 3 numbers.
# So at most we are looping over the array 2 times

# time: O(2n) -> O(n)
# space O(1)
def threeNumberSort(array, order):
	last_idx = 0
	for target in order[:-1]:
		for i in range(last_idx, len(array)):
			if array[i]==target:
				swap(array, i, last_idx)
				last_idx += 1
	return array

def swap(array, idx_1, idx_2):
	array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
