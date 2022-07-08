from calendar import c
from itertools import count
from turtle import st


def solution(s):
    answer = 10000
    for criterion in range(1,len(s)//2 + 1):
        res = ""
        count = 1
        tmp = s[:criterion]

        for i in range(criterion, len(s)+criterion, criterion):
            if tmp == s[i : i + criterion]:
                count += 1
            else:
                if count == 1:
                    res += tmp
                else:
                    res += str(count) + tmp
                    tmp = s[i : i + criterion]
                    count = 1
        answer = min(answer, len(res))
    return answer
         
print(solution("aabbaccc"))