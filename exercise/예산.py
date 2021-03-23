def solution(d, budget):
    answer = 0
    dp = [0]*len(d)
    d.sort()
    sum_d = 0
    for i in range(len(d)):
        sum_d += d[i]
        if budget >= sum_d :
            answer += 1
    return answer

print(solution([2,2,3,3],10))