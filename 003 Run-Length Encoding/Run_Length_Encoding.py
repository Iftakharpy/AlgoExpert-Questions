# time O(n)
# space O(n)
def runLengthEncoding(string):
    if string=='':
        return ''
    enc = []
    idx = 0
    count = 0
    prev_ch = ''
    while idx<len(string):
        ch = string[idx]
        if count == 9:
            enc.append(f"{count}{prev_ch}")
            count = 0
        elif prev_ch!=ch and prev_ch!='':
            enc.append(f"{count}{prev_ch}")
            count = 0
        prev_ch = ch
        idx+=1
        count+=1
    else:
        enc.append(f"{count}{prev_ch}")
    return ''.join(enc)
