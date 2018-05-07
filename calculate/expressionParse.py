# https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing.htm
def calc(l):
    """
    without using operands + - * / to calculate a formula
    input ['+', ['+', 2, 3], ['-', 4, 1]]
    """
    if isinstance(l, (int,long,float,complex)):
        return l
    if l[0] == '+':
        return calc(l[1]) + calc(l[2])
    if l[0] == '-':
        return calc(l[1]) - calc(l[2])
    if l[0] == '*':
        return calc(l[1]) * calc(l[2])
    if l[0] == '/':
        return calc(l[1]) / float(calc(l[2]))


# https://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number

# isinstance(x, (int,long,float,complex))
# or as below using numbers module

import numbers

def calc2(s):
    if isinstance(s[1], numbers.Number):
        a = s[1]
    else:
        a = calc(s[1])
    if isinstance(s[2], numbers.Number):
        b = s[2]
    else:
        b = calc(s[2])

    if s[0] == '+':
        return a+b
    if s[0] == '-':
        return a-b
    if s[0] == '*':
        return a*float(b)
    if s[0] == '/':
        return a/float(b)


# https://classes.cs.uoregon.edu/15W/cis210/assignments/Assnmt10-Symcalc.php
# How to parse an expression to get input
# http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

if __name__=='__main__':
    l = ['/', ['+', 2.0, 3.0], ['-', 4.0, 1.0]]
    print calc(l)

    s = ('*', ('/', 1, 2), ('-', ('+', 5, ('/', 100, 10)), 5))
    print(calc2(s))
