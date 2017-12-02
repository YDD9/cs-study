def addBin(a, b):
    """
    a: str for a bin number
    b: str for a bin number
    s: str for a bin number
    s = a + b
    https://leetcode.com/problems/add-binary/discuss/
    """
    lastA, lastB = len(a)-1, len(b)-1
    c = 0
    s = ''
    while lastA >= 0 or lastB >= 0 or c:
        valA = valB = 0
        if lastA >= 0:
            valA = 1 if a[lastA] == '1' else 0
            lastA -= 1
        if lastB >= 0:
            valB = 1 if b[lastB] == '1' else 0
            lastB -= 1

        c, val = divmod(valA + valB + c, 2)
        s = '%d' % val + s

    return s

def addBin2(a, b):
    return bin(int(a,2) + int(b, 2))[2:]
    # or a slower solution
    # return bin(eval('0b'+a+'+0b'+b))[2:]

if __name__=='__main__':
    print(addBin('11', '1'))
    print(addBin2('11', '1'))
