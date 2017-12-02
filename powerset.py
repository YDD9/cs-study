l = 'abc'

def powerset(xs):
    """
    loop over each char:
    Step 1:
    take first char 'a'
    loop over result [[]]
    result extend with'a'
    result = [[], ['a']]
    2 ** 1 = 2
    Step 2:
    take second char 'b'
    loop over result [[], ['a']]
    result extend with 'b'
    result = [[], ['a'], ['b'], ['a','b']]
    2 ** 2 = 4
    Step 3:
    take third char 'c'
    loop over result [[], ['a'], ['b'], ['a','b']]
    result extend with 'c'
    result = [[], ['a'], ['b'], ['a','b'], ['c'], ['a','c'], ['b','c'], ['a', 'b', 'c']]
    2 ** 3 = 8
    """
    result = [[]]
    for x in xs:
        newset = [[x]+subset for subset in result]
        result.extend(newset)
    return result


def powerset2(xs):
    """
    a   b   c
    ------------
    0   0   0   # 0  ====> ''
    0   0   1   # 1  ====> 'c'
    0   1   0   # 2  ====> 'b'
    0   1   1   # 3  ====> 'bc'
    1   0   0   # 4  ====> 'a'
    1   0   1   # 5  ====> 'ac'
    1   1   0   # 6  ====> 'ab'
    1   1   1   # 7  ====> 'abc'

    For each char in set xs: it has two posibilities, exist(0b1) or not(0b0) in a single subset, total number of subsets is 2**3 = 8, in general 2**n
    So the upper range of our 1st loop is: [0b0 ~ 0b1000), 0b1000 (8==1 << 3), in general presented by bitwise operation 1 << n

    For each step in the 1st loop, we must know which bit is 0b1, as it indicates that char is present in this subset
    So we need a 2nd loop: looping over each bits, here is 3 as we have 3 char in sets xs, in general n
    We still use bitwise operation to find the flip of bits: check last bit 0b101 & 0b001 = 1, check middle bit 0b101 & 0b010 = 0 (False), check first 0b101 & 0b100 = 1 (True)
    """
    n = len(xs)
    result = []
    for i in range(0, 1<<n):
        subset = ''
        for j in range(n):
            if i & (1<<j):
                subset += xs[j]
        result.append(subset)
    return result

print powerset(l)
print powerset2(l)

# Reference
# https://www.youtube.com/watch?v=8cGQ9ocLYCU
# http://www.geeksforgeeks.org/finding-all-subsets-of-a-given-set-in-java/
# https://sevko.io/articles/power-set-algorithms/