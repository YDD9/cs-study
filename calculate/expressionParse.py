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
        return calc(l[1]) / calc(l[2])

if __name__=='__main__':
    l = ['/', ['+', 2.0, 3.0], ['-', 4.0, 1.0]]
    print calc(l)

