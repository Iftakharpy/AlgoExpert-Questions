START = 97
# time O(n)
# space O(n)
# where n is len(string)
def caesarCipherEncryptor(string, key):
    enc = []
    for ch in string:
        enc.append(chr(START + (((ord(ch)-START)+key)%26)))
    return ''.join(enc)
