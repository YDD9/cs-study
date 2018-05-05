# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
def queue(instruct, q=[]):
    if len(instruct) == 2 and instruct[0]=='1':
        q.append(int(instruct[1]))
    elif instruct[0]=='2':
        q.pop(0)
    elif instruct[0]=='3':
        print(q[0])
    else:
        return


if __name__ == '__main__':
    N = int(raw_input().strip())
    for _ in xrange(N):
        row = raw_input().strip().split(' ')
        queue(row)