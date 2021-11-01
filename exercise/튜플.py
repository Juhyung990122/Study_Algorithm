def solution(s):
    answer = []
    tup = {}
    s = s[2:-2].split("},{")    
    for i in s:
        for j in i.split(","):
            if j not in tup:
                tup[j] = 1
            else:
                tup[j] += 1 
    sort_tup = sorted(tup.items(), key=lambda x : x[1],reverse=True)
    for key,value in sort_tup:
        if key.isdigit():
            answer.append(int(key))
    return answer
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))