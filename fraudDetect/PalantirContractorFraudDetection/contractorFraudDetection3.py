class contractorFraudDetection():
    def __init__(self, inputDir):
        # with open(inputDir, 'r') as f:
        #     self.data = f.readlines()
        self.data = inputDir.split('\n')

    def printFraud(self):
        invoiceLimit = -float('inf')
        records = dict()
        for lineNb, line in enumerate(self.data):
            line = line.strip('\n')
            contractor = line.rsplit(';')[0]
            invoiceInfo = line.rsplit(';')[1]
            # case of start
            if invoiceInfo == 'START':
                if contractor in records:
                    records[contractor].append((invoiceLimit,lineNb+1))
                else:
                    records[contractor] = [(invoiceLimit, lineNb+1)]
            else:
                invoiceIds = sorted(map(int, invoiceInfo.rsplit(',')))
                invoiceRecs = sorted(records[contractor])
                nbOfRecs = len(invoiceIds)
                # case of signle submission
                if nbOfRecs == 1:
                    invoiceId = invoiceIds[0]
                    if invoiceId < invoiceRecs[0][0]:
                        print('{};{};SHORTENED_JOB'.format(records[contractor][0][1], contractor))
                    invoiceLimit = max(invoiceId, invoiceLimit)
                    del records[contractor][0]
                # case of batch submission
                else:
                    if invoiceIds[-1] < invoiceRecs[0][0]:
                        for r in range(nbOfRecs):
                            print('{};{};SHORTENED_JOB'.format(invoiceRecs[r][1], contractor))
                    elif sum([invoiceIds[i] >= invoiceRecs[i][0] for i in range(nbOfRecs)]) == nbOfRecs:
                        pass # no fraud no screen print
                    else:
                        print('{};{};SUSPICIOUS_BATCH'.format(lineNb+1, contractor))
                    invoiceLimit = max(invoiceIds[-1], invoiceLimit)
                    del records[contractor][:nbOfRecs]

if __name__=='__main__':






# 9;Evil; 24 is the limit and allowed the equal case
# 11;Evil;SHORTENED_JOB
    strInput = """Alice;START
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





# all pass no output
    strInput = """Tom;START
Jeremy;START
David;START
Jeremy;4
David;3
James;START
Matt;START
James;6
Nick;START
Tom;2
Matt;5
Nick;7"""







# 8;Jeremy;SUSPICIOUS_BATCH
    strInput = """Nick;START
Jeremy;START
Leah;START
Nick;10
Jeremy;START
Jeremy;START
Leah;15
Jeremy;8,9,14"""
# input.8.txt
# 7;L;SHORTENED_JOB
    strInput8 = """T;START
J;START
D;START
J;4
D;2
J;START
L;START
J;5
N;START
T;1
N;6
L;3"""
# input.9.txt
# 11;Jeremy;SUSPICIOUS_BATCH
    strInput9 = """Jeremy;START
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





# # input.10.txt
#     strInput = """L;START
# L;10
# A;START
# A;START
# A;START
# A;8,9,10"""
    strInput10 = """Nick;START
Jeremy;START
Leah;START
Nick;10
Jeremy;START
Jeremy;START
Leah;15
Jeremy;8,14,9"""  # input.10.txt  8;Jeremy;SUSPICIOUS_BATCH
    # detFraud = contractorFraudDetection('fraudDetect\PalantirContractorFraudDetection\input.txt')
    detFraud = contractorFraudDetection(strInput9)
    detFraud.printFraud()
    print('Detection finished by Imp3.')
    # https://github.com/AntonioL/catching-an-insider-trader/blob/master/catching_an_insider_trader.py