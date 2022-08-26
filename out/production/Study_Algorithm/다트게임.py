def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10","A")
    mul = {'S': 1, 'D': 2, 'T': 3}

    for i in dartResult:
        #숫자면
        if i.isdigit() or i == "A":
            stack.append(10 if i == "A" else int(i))
        elif i in ("S","D","T"):
            num = stack.pop()
            stack.append(num**mul[i])
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            num = stack.pop()
            if len(stack) != 0:
                stack[-1] *= 2
            stack.append(num * 2)

    return sum(stack)

print(solution("1S2D*3T"))