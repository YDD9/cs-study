class ContractorFraudDetection():
    def __init__(self, inputDir):
        # with open('fraudDetect\PalantirContractorFraudDetection\input.txt', 'r') as f:
        with open(inputDir, 'r') as f:
            self.data = f.readlines()

    def printFraud(self):
        # set initially invoice_limit -inf to accept all invoice_id
        # once a bigger invoice_id submitted(no matter fraud or not), assign it to invoice_limit
        # from then any newly start contractor must submit bigger invoice_id than invoice_limit
        records = dict(invoice_limit=-float('inf'))
        # records stores contractor_id(key);
        # stores contractor's invoice_limit and last START line number together in a list(value)

        for lineNb, line in enumerate(self.data):
            line = line.replace('\n','')
            contractor_id = line.rsplit(';')[0]
            # contractor start
            if line.rsplit(';')[1] == 'START':
                records[contractor_id] = [records['invoice_limit']]
                records[contractor_id].append(lineNb+1)
            # contractor submit
            else:
                # contractor single submit
                if len(line.rsplit(';')[1].rsplit(',')) == 1:
                    invoice_id = int(line.rsplit(';')[1].rsplit(',')[0])
                    if records['invoice_limit'] <= invoice_id:
                        records['invoice_limit'] = invoice_id
                    # submitted invoice_id is smaller than his allowed limit
                    if records[contractor_id][0] > invoice_id:
                        print('{};{};SHORTENED_JOB'.format(records[contractor_id][1], contractor_id))
                # contractor batch submit
                else:
                    for invoice_id in line.rsplit(';')[1].rsplit(','):
                        invoice_id = int(invoice_id)
                        if records['invoice_limit'] <= invoice_id:
                            records['invoice_limit'] = invoice_id
                        # submitted invoice_id is smaller than his allowed limit
                        if records[contractor_id][0] > invoice_id:
                            print('{};{};SUSPICIOUS_BATCH'.format(lineNb+1, contractor_id))
                            # at least one violation in batch, suspicious contractor is found
                            break

if __name__=='__main__':
    detect = ContractorFraudDetection('fraudDetect\PalantirContractorFraudDetection\input.txt')
    detect.printFraud()
    print('Detection finished.')