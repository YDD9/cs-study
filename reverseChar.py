def reversechar(myStr):
    l = 0
    r = len(myStr)-1

    res = list(myStr)

    while l <= r:
        if not myStr[l].isalpha():
            l += 1
        elif not myStr[r].isalpha():
            r -= 1
        else:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

    return ''.join(res)


print reversechar('a,toc')