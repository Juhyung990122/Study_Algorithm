def solution(s):
    answer = 0
    result = ""
    for i in range(1,len(s)//2+1):
        count = 1
        tmp = s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i] == tmp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count)+tmp
                tmp = s[j:j+i]
                count = 1
        print(result)          
    return answer
print(solution("aabbaccc"))