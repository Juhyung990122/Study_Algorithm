def solution(n, stages):
    answer = []
    success = [0] * n

    for i in range(len(stages)):
        for j in range(stages[i]):
            if j == n:
                break
            success[j] += 1
    print(success)

    
    for i in range(1,n+1):
        print(stages.count(i),success[i-1])
        if success[i-1] == 0: 
            if stages.count(i) == 0:
                answer.append([i,0.0])
                continue
        
        answer.append([i,stages.count(i)/success[i-1]]) 

    answer.sort(key=lambda x : x[1] ,reverse=True)
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    
    return answer
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))