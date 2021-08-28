def solution(code, day, data):
    answer = []
    data_list = list()
    answer_list = list()
    for i in data:
        p,c,t = i.split()
        p = int(p[6:])
        c = c[5:]
        t = t[5:]
        data_list.append([p,c,t])
    
    for i in data_list:
        if i[1] == code:
            if i[2][:-2] == day:
                answer_list.append((i[0],i[2]))
    answer_list.sort(key=lambda x : x[1])
    for i in answer_list:
        answer.append(i[0])
    return answer

print(solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))