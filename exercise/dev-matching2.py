def solution(enroll, referral, seller, amount):
    answer = []
    relation = dict()
    income = dict()
    for i in range(len(enroll)):
        relation[enroll[i]] = referral[i]
        income[enroll[i]] = 0
    
    for s in range(len(seller)):
        income[seller[s]] += amount[s] * 100
        now_income = amount[s]*100
        while True:
            if relation[seller[s]] == '-':
                print('start - ',seller[s],income[seller[s]])
                income[seller[s]] -= int(amount[s]*10)
                break
            
            now = relation[seller[s]]
            print(seller[s],now)
            r_income = now_income * 0.1
            now_income = r_income
            income[seller[s]] -= r_income
            income[now] += r_income
            seller[s] = relation[seller[s]]
            print(seller[s],r_income)
            if relation[seller[s]] == '-':
                print('done',seller[s],r_income,int(r_income*0.1))
                income[seller[s]] -= int(r_income*0.1)
                break
        print(income)

    for people in relation:
        answer.append(int(income[people]))
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "-", "-" ,"-", "-", "-", "-"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))