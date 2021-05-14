from collections import deque

def solution(S):
    try:
        S = list(S.split())
        stack = deque()
        i = 0
        while True:
            if i == len(S):
                return stack[-1]
            now = S[i]
            if now == "POP":
                stack.pop()
            elif now == "DUP":
                stack.append(stack[-1])
            elif now == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif now == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(x-y)
            else:
                stack.append(int(now))
            i += 1

    except IndexError:
        return -1


print(solution('5 6 + -'))