
def gen_form_data(raw_data):
    form_data = dict()
    temp=0
    for index, line in enumerate(raw_data):
        # try:
        if temp==index:
            case_nb = int(line)
            entry_nb = int(raw_data[index+1])
            # 1<= entry_nb <= 10**6
            form_data[case_nb] = raw_data[index+2 : index+2+entry_nb]
            temp = index + 2 + entry_nb
        else:
            continue
        # except:
        #     pass
    return form_data


def print_all_customers(form_data):
    uniq_cus = set()
    for i in form_data.keys():
        for j in range(len(form_data[i])):
            uniq_cus.add(form_data[i][j].rsplit(',')[5])
    for customer in sorted(uniq_cus):
        print(customer)


def print_cus_repeat_fraud(form_data):
    cus_mer = dict()
    for i in form_data.keys():
        for j in range(len(form_data[i])):
            cus = form_data[i][j].rsplit(',')[5]
            mer = form_data[i][j].rsplit(',')[-1].replace("\n","")
            if cus not in cus_mer:
                cus_mer[cus]= dict()
                cus_mer[cus][mer] = 1
            elif mer in cus_mer[cus]:
                cus_mer[cus][mer] += 1
            else:
                cus_mer[cus][mer] = 1
    res=[]
    for cus in cus_mer:
        for mer in cus_mer[cus]:
            if cus_mer[cus][mer] >= 5:
                res.append(cus)
    print(sorted(res))
    # return cus_mer

def print_cus_two_plus_count(form_data):
    cus_count = {}
    for i in form_data.keys():
        for j in range(len(form_data[i])):
            cus = form_data[i][j].rsplit(',')[5]
            count = form_data[i][j].rsplit(',')[3]
            if cus not in cus_count:
                cus_count[cus]= []
                cus_count[cus].append(count)
            elif count not in cus_count[cus]:
                cus_count[cus].append(count)
            else:
                pass
    res=[]
    for cus in cus_count:
        if len(cus_count[cus]) >=2 :
            res.append(cus)
    print(sorted(res))
    # return cus_mer

def print_cus_higher_median_fraud(form_data):
    total_scores = 0
    total_transfer = 0
    cus_score = {}
    res=[]
    for i in form_data.keys():
        for j in range(len(form_data[i])):
            cus = form_data[i][j].rsplit(',')[5]
            score = int(form_data[i][j].rsplit(',')[0])
            total_transfer += 1
            total_scores += score
            if cus not in cus_score:
                cus_score[cus] = []
                cus_score[cus].append(score)
            else:
                cus_score[cus].append(score)
    avg_fraud = float(total_scores)/total_transfer
    for cus in cus_score:
        for score in cus_score[cus]:
            if score > avg_fraud:
                res.append(cus)
                break

    print(sorted(res))


def total_fraud(form_data):
    res = 0
    for i in form_data.keys():
        for j in range(len(form_data[i])):
            cus = form_data[i][j].rsplit(',')[5]
            amount = int(form_data[i][j].rsplit(',')[4])
            fraud = form_data[i][j].rsplit(',')[2]
            if fraud:
                res += amount
    return res

if __name__=='__main__':

    testing = 0

    with open('fraudDetect\data.txt', 'r') as f:
        raw_data = f.readlines()

    if testing: print(raw_data)

    form_data = gen_form_data(raw_data)

    if testing: print(form_data)

    print("Question1:")
    print_all_customers(form_data)

    print("Question2:")
    print_cus_repeat_fraud(form_data)

    print("Question3:")
    print_cus_higher_median_fraud(form_data)

    print("Question4:")
    print_cus_two_plus_count(form_data)

    print("Question5:")
    print(total_fraud(form_data))

