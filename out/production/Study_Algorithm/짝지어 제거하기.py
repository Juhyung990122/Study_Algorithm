from collections import deque
def solution(s):
    answer = 0
    s = list(s)
    stack = deque()
    index = 0
    while index <= len(s)-1:
        stack.append(s[index])
        index += 1
        if len(stack) == 1:
            continue
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if stack:
        return 0
    else: 
        return 1

print(solution("baabaa"))