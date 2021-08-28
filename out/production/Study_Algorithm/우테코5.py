def solution(totalTicket, logs):
    answer = 0
    log = dict()
    for i in logs:
        i_split = i.split(' ')        
        log[i_split[0]] = list()
    for j in logs:
        j_split = j.split(' ')
        log[j_split[0]].append(j_split[2]) 

    #초기화 완료 내일 나머지 구현할 것.        


    return answer
print(solution(2000,
["woni request 09:12:29",
"brown request 09:23:11",
"brown leave 09:23:44",
"jason request 09:33:51",
"jun request 09:33:56",
"cu request 09:34:02"
]))