# Complete the function below.
testing = 0

def findViolations(datafeed):
    res = []
    curLimit = -float('inf')
    records = dict()
    if testing: print(datafeed)
    for irow, line in enumerate(datafeed):
        contractor = line.split(';')[0]
        if line.split(';')[1]=='START':
            if contractor in records:
                records[contractor].append((curLimit, irow+1))
            else:
                records[contractor] = [(curLimit, irow+1)]
        else:
            sub = sorted(map(int, line.split(';')[1].split(',')),reverse=True)
            nbSub = len(sub)
            recs = sorted(records[contractor],reverse=True)
            # single submission
            if nbSub == 1:
                if sub[0] < recs[0][0]:
                    res.append('{};{};SHORTENED_JOB'.format(recs[0][1], contractor))
                curLimit = max(curLimit, sub[0])
                del records[contractor][0]
            else:
                if sub[0] < recs[-1][0]:
                    for r in range(nbSub):
                        res.append('{};{};SHORTENED_JOB'.format(recs[r][0], contractor))
                elif sum([sub[j]>=recs[j][0] for j in range(nbSub)])==nbSub:
                    pass
                else:
                    l = list(recs)
                    for x in range(nbSub):
                        toBeDel= []
                        for y in range(len(l)):
                            if sub[x] < l[y][0]:
                                res.append('{};{};SHORTENED_JOB'.format(l[y][1], contractor))
                            else:
                                toBeDel.append(y)
                                break
                            toBeDel.append(y)
                        tmp = []
                        for i in range(len(l)):
                            if i not in toBeDel:
                                tmp.append(l[i])
                        l = list(tmp)
                    res.append('{};{};SUSPICIOUS_BATCH'.format(irow+1, contractor))
                curLimit = max(curLimit, sub[0])
                del records[contractor][:nbSub]
    return res

f1="""Alice;START
Bob;START
Bob;1
Carson;START
Alice;15
Carson;6
David;START
David;24
Evil;START
Evil;24
Evil;START
Evil;18
Fiona;START"""

f6="""Nick;START
Jeremy;START
Leah;START
Nick;10
Jeremy;START
Jeremy;START
Leah;15
Jeremy;8,14,9"""



f8="""Jeremy;START
Leah;START
Leah;50
Jeremy;START
Leah;START
Leah;100
Jeremy;START
Leah;START
Leah;150
Jeremy;START
Jeremy;37,52,68,86
John;START
John;START
John;500,5000"""

# 7;Jeremy;SHORTENED_JOB
# 10;Jeremy;SHORTENED_JOB
# 11;Jeremy;SUSPICIOUS_BATCH
print findViolations(f6.split('\n'))