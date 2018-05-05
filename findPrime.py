from math import sqrt
def prime(N):
    # 0 and 1 are not prime
    res = [False, False] + [True] * (N-1)
    for i in range(2, int(sqrt(N))+1):
        pointer = i*i
        while pointer<= N:
            res[pointer] = False
            pointer += i
    out = [i for i in range(N+1) if res[i]]
    return res, out


def prime2(N):
    sieve, out = [False, False] + [True] * (N-1), []
    for p in range(2, N+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p*p, N+1, p):
                sieve[i] = False
    return sieve, out

# N must bigger than 2
N = 20

print prime(N)
print prime2(N)


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for t in range(3, int(math.sqrt(n)+1),2):
        if n % t == 0:
            return False
    return True

print [n for n in range(100) if isPrime(n)]