# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # time O(n) | space O(n) - n is len(string) - start_index
    def insertSuffixStartingAtIndex(self, start_index, string):
        trie = self.root
        for idx in range(start_index, len(string)):
            ch = string[idx]
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]
        trie[self.endSymbol] = True

    # time O(n^2) | space O(n^2) - n is len(string)
    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insertSuffixStartingAtIndex(idx, string)

    # time (m) | space O(1) - m is len(string)
    def contains(self, string):
        trie = self.root
        for ch in string:
            if ch not in trie:
                return False
            trie = trie[ch]
        return self.endSymbol in trie
