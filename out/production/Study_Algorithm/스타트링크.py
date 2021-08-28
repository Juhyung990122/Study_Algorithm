import sys
from collections import deque

f,s,g,u,d = map(int,sys.stdin.readline().split())

total = f
end = g
now = s

def dfs(start):
    visited = [1]+[0] * (f)
    visited[start] = 1
    stack = deque()
    stack.append(start)
    count = 0 
    pre_n = 0
    while stack:
        n = stack.pop()
        if pre_n == n:
            return 'use the stairs'
        if n == g:
            return count
        # 내려가는 경우
        if n > g and n - d > 0 or n + u > g: 
            if visited[n - d] == 0:
                stack.append(n - d)
                visited[n - d] = 1
                count += 1
                pre_n = n
        #올라가는 경우
        elif n < g and n + u <= f or n - d > 0:
            if visited[n + u] == 0:
                stack.append(n + u)
                visited[n + u] = 1
                count += 1
                pre_n = n
    return 'use the stairs'
       
print(dfs(s))