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


# time O(n)
# space O(1)
def threeNumberSort(array, order):
	first_value = order[0]
	second_value = order[1]
	
	# positions of the numbers in order
	first_idx, second_idx, third_idx = 0, 0, len(array)-1
	
	while second_idx <= third_idx:
		value = array[second_idx]
		
		if value == second_value:
			second_idx += 1
		elif value == first_value:
			swap(array, first_idx, second_idx)
			first_idx += 1
			second_idx += 1
		else:
			swap(array, second_idx, third_idx)
			third_idx -= 1
	return array


# time O(n)
# space O(1)
def threeNumberSort(array, order):
	first = order[0]
	third = order[-1]
	first_idx = 0
	third_idx = len(array) - 1
	
	idx = 0
	while idx<=third_idx:
		if first == array[idx]:
			swap(array, first_idx, idx)
			first_idx += 1
			idx += 1
		elif third == array[idx]:
			swap(array, third_idx, idx)
			third_idx -= 1
			# Here not increasing the idx.
			# Because the number swapped from the third_idx isn't necessarily in the correct place yet.
		else:
			# It's the second number so it's in the correct place
			idx+=1
	return array
