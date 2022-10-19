from re import T


def solution(s,t):
    answer = 0
    while True:
        split_s = str(s).replace(t, "")
        if len(s) == len(split_s):
            return answer
        answer += 1
        s = split_s

print(solution("aaaaabbbbb","ab"))