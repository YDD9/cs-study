def calcPower(x, y):
    # x**y
    if y == 0:
        return 1
    if y == 1:
        return x

    tempX = x
    while y > 1:
        sum = 0
        for i in range(x):
            sum += tempX
        tempX = sum
        y -= 1
    return sum

print calcPower(2, 1)
print calcPower(2, 0)
print calcPower(5, 4)
print("====================")

# https://www.youtube.com/watch?v=OIgpvFAew6k

def calcPower2(x, y):
    if y == 0:
        return 1
    tempX = x
    ans = x
    for i in range(y-1):
        for j in range(x-1):
            ans += tempX
        tempX = ans

    return ans
        
print calcPower2(4, 0)
print calcPower2(4, 1)
print calcPower2(4, 4)
print("====================")
