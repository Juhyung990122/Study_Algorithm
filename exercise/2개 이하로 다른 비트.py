def convert(n):
    a = [0 for _ in range(300)]
    i = -1
    while n > 0:
        a[i] = n % 2
        n //= 2
        i -= 1
    return a

def solution(numbers):
    answer = []
    for i in numbers:
        num = convert(i)
        if i % 2 == 0:
            num[-1] = 1
        else:
            for j in range(len(num)-1,0,-1):
                if num[j] == 0:
                    num[j] = 1
                    num[j+1] = 0
                    break
        convert_to_ten = 0
        for i in range(len(num)):
            if num[i] == 1:
                convert_to_ten += 2 ** (len(num)-1-i)
        answer.append(convert_to_ten)
    return answer

print(solution([2,7]))