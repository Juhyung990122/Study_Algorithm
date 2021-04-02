
def solution(pobi,crong):
    answer = 0
    pobi_score = [[],[]]
    crong_score = [[],[]]
    score_list = []

    def multiply(arr):
        ans = 1
        for n in arr:
            if n == 0:
                return 0
            ans *= n
        return ans

    if pobi[0] + 1 != pobi[1]:
        return -1
    if crong[0] + 1 != crong[1]:
        return -1

    for i in range(2):
        if pobi[i] // 100 != 0:
            pobi_score[i].append(pobi[i] // 100) 
        pobi[i] %= 100
        if pobi[i] // 10 != 0:
            pobi_score[i].append(pobi[i] // 10)
        pobi[i] %= 10
        pobi_score[i].append(pobi[i] // 1) 
        if crong[i] // 100 != 0:
            crong_score[i].append(crong[i] // 100) 
        crong[i] %= 100
        if crong[i] // 10 != 0:
            crong_score[i].append(crong[i] // 10)
        crong[i] %= 10
        crong_score[i].append(crong[i] // 1) 

    pobi = max(sum(pobi_score[0]),sum(pobi_score[1]),multiply(pobi_score[0]),multiply(pobi_score[1]))
    crong = max(sum(crong_score[0]),sum(crong_score[1]),multiply(crong_score[0]),multiply(crong_score[1]))
    if pobi == crong : 
        return 0
    elif pobi > crong:
        return 1
    elif pobi < crong:
        return 2
    else:
        return 0

print(solution([99,102],[211,212]))
