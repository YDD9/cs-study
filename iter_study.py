with open('text.txt', 'r') as fp:
    print type(fp)
    print type(fp.readline)
    for line in iter(fp.readline, ''):
        print line