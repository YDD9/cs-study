class ContractorFraudDetection():
    # def __init__(self):
    #     self.n_data = int(raw_input())
    def __init__(self, inputDir):
        with open(inputDir, 'r') as f:
            self.data = f.readlines()

    def printFraud(self):
        # set initially invoice_limit -inf to accept all invoice_id.
        # once a bigger invoice_id submitted(no matter fraud or not), assign it to invoice_limit.
        # from then any newly start contractor should submit bigger invoice_id than invoice_limit;
        # othwerwise fraud or suspicious
        invoice_limit=-float('inf')

        records = dict()
        # records dict stores contractor_id(key);
        # stores inside a list(value) tuple of contractor's invoice_limit and corresponding START line number

        # lineNb = 0
        # for line in range(self.n_data):
        #     line = raw_input()
        for lineNb, line in enumerate(self.data):
            line = line.replace('\n','')

            contractor_id = line.rsplit(';')[0]
            # contractor start
            if line.rsplit(';')[1] == 'START':
                if contractor_id in records:
                    records[contractor_id].append((invoice_limit, lineNb+1))
                else:
                    records[contractor_id]=[(invoice_limit, lineNb+1)]
            # contractor submit
            else:
                # contractor single submit
                if len(line.rsplit(';')[1].rsplit(',')) == 1:
                    invoice_id = int(line.rsplit(';')[1].rsplit(',')[0])
                    invoice_limit = max(invoice_limit, invoice_id)
                    # submitted invoice_id is smaller than his allowed limit
                    if invoice_id < records[contractor_id][0][0]:
                        print('{};{};SHORTENED_JOB'.format(records[contractor_id][0][1], contractor_id))
                    del records[contractor_id][0]
                # contractor batch submit
                else:
                    invoice_ids = sorted(map(int, line.rsplit(';')[1].rsplit(',')))
                    contractor_lims = sorted(records[contractor_id])
                    invoice_limit = max(contractor_lims[-1][0],invoice_limit)
                    nbOfSubm = len(contractor_lims)
                    # max invoice_id smaller than min contractor limit
                    if invoice_ids[-1] <= contractor_lims[0][0]:
                        for i in range(nbOfSubm):
                            print('{};{};SHORTENED_JOB'.format(records[contractor_id][i][1], contractor_id))
                    elif sum([invoice_ids[i]>contractor_lims[i][0] for i in range(nbOfSubm)]) == nbOfSubm:
                        # no fraud, no output
                        pass
                    else:
                        print('{};{};SUSPICIOUS_BATCH'.format(lineNb+1, contractor_id))
                    del records[contractor_id][:nbOfSubm]

                    # for invoice_id in line.rsplit(';')[1].rsplit(','):
                    #     invoice_id = int(invoice_id)
                    #     if records['invoice_limit'] <= invoice_id:
                    #         records['invoice_limit'] = invoice_id
                    #     # submitted invoice_id is smaller than his allowed limit
                    #     if records[contractor_id][0] > invoice_id:
                    #         print('{};{};SUSPICIOUS_BATCH'.format(lineNb+1, contractor_id))
                    #         # at least one violation in batch, suspicious contractor is found
                    #         break

            # lineNb += 1

if __name__=='__main__':
    # detect = ContractorFraudDetection()
    detect = ContractorFraudDetection('fraudDetect\PalantirContractorFraudDetection\input.txt')
    detect.printFraud()
    print('Detection finished by Imp2.')