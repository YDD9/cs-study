class ContractorFraudDetection():
    def __init__(self, inputDir):
        # with open('fraudDetect\PalantirContractorFraudDetection\input.txt', 'r') as f:
        with open(inputDir, 'r') as f:
            self.data = f.readlines()

    def printFraud(self):
        records = dict(currMin=-float('inf'))
        for lineNb, line in enumerate(self.data):
            line = line.replace('\n','')
            contractor_id = line.rsplit(';')[0]
            if line.rsplit(';')[1] == 'START':
                records[contractor_id] = [records['currMin']]
                records[contractor_id].append(lineNb+1)
            else:
                invoice_id = line.rsplit(';')[1].rsplit(',')
                if contractor_id in records:
                    if len(invoice_id) <= 1:
                        invoice_id = int(invoice_id[0])
                        if records['currMin'] <= invoice_id:
                            records['currMin'] = invoice_id
                        # elif invoice_id < records['currMin']:
                        #     records['currMin'] = invoice_id
                        if records[contractor_id][0] > invoice_id:
                            print('{};{};SHORTENED_JOB'.format(records[contractor_id][1], contractor_id))
                    else:
                        for invoice_id in records[contractor_id]:
                            invoice_id = int(invoice_id)
                            if records['currMin'] <= invoice_id:
                                records['currMin'] = invoice_id
                            if records[contractor_id][0] > invoice_id:
                                print('{};{};SUSPICIOUS_BATCH'.format(lineNb+1, contractor_id))

if __name__=='__main__':
    detect = ContractorFraudDetection('fraudDetect\PalantirContractorFraudDetection\input.txt')
    detect.printFraud()
    print('Detection finished.')