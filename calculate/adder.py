# http://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
def adder(A, B):
    while B != 0:
        carry = A & B
        A = A ^ B
        B = carry << 1
    return A

print(adder(3, -5))
print(adder(-3, -5))
print(adder(3, -4294967295L))
print('============')


# http://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
def subtractor(x, y):
    # x - y
    while y != 0:
        borrow = ~x & y
        x = x ^ y
        y = borrow << 1
    return x

print(subtractor(5, -3))
print('================')

# Decimal --> binary conversion https://stackoverflow.com/questions/1395356/how-can-i-make-bin30-return-00011110-instead-of-0b11110
print(format(10, '#b'))
print(format(10, 'b'))
print(bin(10).lstrip('-0b').zfill(8))
print(int('1010',2))
print('================')

# https://discuss.leetcode.com/topic/51999/python-solution-with-no-completely-bit-manipulation-guaranteed/3
def adder(a, b):
    N = 8
    # 32 bit max int positive
    maxNum = 2**(N-1)-1
    # 32 bit min int negative
    minNum = -2**(N-1)
    # mask to get last 32 bits
    mask = 2**N-1
    while b!= 0:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = (carry << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative

    return a if a <= maxNum else ~(a ^ mask)
    # Considering the compliment switching on ~(a ^ mask), there's an alternative way to do this, which is (a|~mask). It also helps trim the bits and keeps the value
    # return a if a <= maxNum else a|~mask

print(adder(-2, -3))
# (-5) 1 1 1 1  1 0 1 1
# in Python not (-5) but (251)
# mask 1 1 1 1  1 1 1 1
# ----------------------
# ^ =  0 0 0 0  0 1 0 0 
# in Python (4) is (-5)'s complement positve
# ~4          
# ~4 is -4-1 = (-5) is (4)'s complement negative
# btw: ~-5 = 4