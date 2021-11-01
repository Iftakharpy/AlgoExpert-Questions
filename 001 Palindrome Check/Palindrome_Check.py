# time O(n) - n is len(array)
# space O(1)
def isPalindrome(string):
    left = 0
    right = len(string)-1
    while left<right:
        if not string[left] == string[right]:
            return False
        left+=1
        right-=1
    return True
