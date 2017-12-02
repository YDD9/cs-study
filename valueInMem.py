# l_mem = []

# l = l_mem           # the first call
# for i in range(2):
#     l.append(i*i)

# print(l)            # [0, 1]

# l = [3,2,1]         # the second call
# for i in range(3):
#     l.append(i*i)

# print(l)            # [3, 2, 1, 0, 1, 4]

# l = l_mem           # the third call
# for i in range(3):
#     l.append(i*i)

# print(l)            # [0, 1, 0, 1, 4]



def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 
    del l

f(2)
f(3,[3,2,1])
f(3)






def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

f2(1,2,3)                       # 1 2 (3,) {}
f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}
f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8} 