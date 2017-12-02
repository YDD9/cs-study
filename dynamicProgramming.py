from timeit import default_timer as timer

def factorial(n):
    result = None
    if n == 0:
        return 1
    else:
        result = factorial(n-1) * n
        return result

start = timer()
res = factorial(900)
end = timer()
print('factorial %d cost %r' %(res, end-start))


# def factorial2(n):
#     return reduce(lambda x,y: x*y, [1]+range(1, n+1))

# print factorial2(0)


def factorial3(n):
    lookup = {}
    if n==0:
        return 1
    elif n in lookup:
        return lookup[n]
    else:
        x = factorial3(n-1) * n
        lookup[n] = x
        return x

start3 = timer()
res3 = factorial3(900)
end3 = timer()
print('factorial3 %d cost %r' %(res3, end3-start3))


# how to compare performance and use timeit