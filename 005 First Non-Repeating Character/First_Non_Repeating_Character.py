# time O(n+m) where n is len(string) and m is len(seen)
# space O(n) - O(25) -> O(1) - because we are only lowercase English-alphabet letters
def firstNonRepeatingCharacter(string):
    seen = {}
    for idx, ch in enumerate(string):
        if ch not in seen:
            seen[ch] = {'firstSeenAt': idx, 'count': 1}
        else:
            seen[ch]['count'] += 1
    for _, item in seen.items():
        firstSeenAt, count = item.values()
        if count == 1:
            return firstSeenAt
    return -1
