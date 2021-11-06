# time O(n) where n is len(characters+document)
# space O(k) where k in number of unique characters in characters
def generateDocument(characters, document):
    if document=="":
        return True
    chrs = {}
    for ch in characters:
        if ch not in chrs:
            chrs[ch] = 1
        else:
            chrs[ch] += 1
    for ch in document:
        if ch not in chrs:
            return False
        else:
            chrs[ch]-=1
            if chrs[ch]<0:
                return False
    return True
