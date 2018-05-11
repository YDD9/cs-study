# Given an expression like ABC + CDE = EFG,
# I was asked to check if certain values for each letter would solve the expression.
# https://www.quora.com/What-is-an-algorithm-for-generating-all-possible-combinations-of-a-given-set-of-letters-e-g-a-b-c-d-e

# https://gist.github.com/dougwt/1969743
# recursive solution and one line solution
# list(itertools.combinations([1, 2, 3], 2))  # C(n, k) no orders
# list(itertools.permutations([1, 2, 3], 2))  # order is considered


def num():
    l = range(10)
    tmp = list(l)
    for iA, A in enumerate(l):
        if A == 0: continue
        for iB, B in enumerate(l):
            if B == A:
                continue
            for iC, C in enumerate(l):
                if C == A or C == B or C == 0:
                    continue
                for iD, D in enumerate(l):
                    if D == A or D == B or D == C:
                        continue
                    for iE, E in enumerate(l):
                        if E == A or E == B or E == C or E == D or C == 0:
                            continue
                        for iF, F in enumerate(l):
                            if F == A or F == B or F == C or F == D or F == E:
                                continue
                            for iG, G in enumerate(l):
                                if G == A or G == B or G == C or G == D or G == E or G == F:
                                    continue
                                if (C+E) % 10 == G and (B+D+(C+E)//10) % 10 == F\
                                    and (A+C+(B+D)//10) == E:
                                    return A,B,C,D,E,F,G

# print(num())

# https://www.youtube.com/watch?v=hqijNdQTBH8
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# https://www.youtube.com/watch?v=nYFd7VHKyWQ&t=1328s
# https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
def perm(a, k=0):
   if k == len(a):
      print a
   else:
      for i in xrange(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm([1,2,3])



# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print p