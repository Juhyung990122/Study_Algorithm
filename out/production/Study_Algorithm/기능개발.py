def solution(progresses, speeds):
    answer = []
    complete = []
    for i in range(len(progresses)):
        c_day = 0
        calculate = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] == 0:
            c_day = calculate
        else:
            c_day = calculate + 1

        complete.append(c_day)


    while len(complete) > 0:
        target = complete[0]
        completed_task = 0
        for i in range(0,len(complete)):
            if target < complete[i] :
                if len(complete[i:]) > 0:
                    complete = complete[i:] 
                break
            if i == len(complete)-1:
                completed_task = len(complete)
                complete = []
                break
            completed_task += 1
        
        answer.append(completed_task)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))