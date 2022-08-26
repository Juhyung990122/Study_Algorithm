from collections import deque
def solution(n, computers):
    con = dict()

    for i in range(n):
        con[i+1] = []

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                con[i+1].append(j+1)

    answer = 0
    queue = deque()
    visited = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i] != 1:
            queue.append(i)
            visited[i] = 1
            while queue:
                now = queue.popleft()
                if con[now]:
                    for j in con[now]:
                        if visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
            answer += 1
    
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))