# Solve using while loop
# time O(n) where n = len(array)
# space O(1)
def isValidSubsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0
    while arr_idx<len(array) and seq_idx<len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx+=1
    return seq_idx==len(sequence)


# Solve using for loop
# time O(n)
# space O(1)
def isValidSubsequence(array, sequence):
    seq_idx = 0
    for num in array:
        if len(sequence) == seq_idx:
            break
        if num == sequence[seq_idx]:
            seq_idx+=1
    return len(sequence) == seq_idx
