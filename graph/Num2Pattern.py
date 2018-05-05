# Given an expression like ABC + CDE = EFG,
# I was asked to check if certain values for each letter would solve the expression.

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

print(num())