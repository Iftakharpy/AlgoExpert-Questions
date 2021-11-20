# time: O(n^2) | space O(1)
def countInversions(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i!=j and array[i] > array[j]:
                inversions += 1
    return inversions
