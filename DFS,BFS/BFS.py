#bfs example
from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
] 
visited = [0] * 9

queue = deque([1])
visited[1] = 1
while queue:
    p = queue.popleft()
    print(p,end=" ")
    for i in graph[p]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1



