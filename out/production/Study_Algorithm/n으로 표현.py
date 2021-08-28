#밥먹고 와서 복기해볼것!

def solution(N, number):
    answer = 0
    if N == number:
        return 1
    dp = list(list() for x in range(8))

    for r,v in enumerate(dp,start=1):
        v.append(int(str(N) * r))
    
    #지금 갱신할 리스트 인덱스 (3개로 만들 수 있는 수들의 집합)
    for i in range(1,8):
        #이전 기록들 들어있는 리스트 인덱스(1개,2개로 만들 수 있는 수들의 집합)
        for j in range(i):
            #(1개로 만들 수 있는 수)(2개로 만들 수 있는 수)
            for op1 in dp[j]:
                #(2개로 만들 수 있는 수)(1개로 만들 수 있는 수)
                for op2 in dp[i-j-1]:
                    dp[i].append(op1+op2)
                    dp[i].append(op1-op2)
                    dp[i].append(op1*op2)
                    if op2 != 0:
                        dp[i].append(op1//op2)       
        if number in dp[i]:
            answer = i+1
            break       
        else:
            answer = -1
    return answer

print(solution(5,12))
