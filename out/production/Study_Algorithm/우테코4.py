def solution(number):
    answer = 0
    for i in range(1,number+1):
        i = str(i)
        if '3' in i:
            answer += i.count('3')
        if '6' in i:
            answer += i.count('6')
        if '9' in i:
            answer += i.count('9')
    return answer
print(solution(33))