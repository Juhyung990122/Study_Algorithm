from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0,0]*n
    graph = dict()
    for i in range(len(computers)):
        graph[i+1] = list()
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                graph[i+1].append(j+1)
    queue = deque()
    for k in range(1,n+1):
        if visited[k] == 0:
            if len(graph[k]) != 0:
                queue.append(k)
                visited[k] = 1
                while queue:
                    pop_c = queue.popleft()
                    for r in range(len(graph[pop_c])):
                        if visited[graph[pop_c][r]] == 0:
                            queue.append(graph[pop_c][r])
                            visited[graph[pop_c][r]] = 1
                answer += 1
            else:
                answer += 1
    return answer
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))