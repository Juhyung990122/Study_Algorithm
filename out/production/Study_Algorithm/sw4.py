import sys
from collections import deque

t = int(sys.stdin.readline())
answer = list()
upper_graph = list()
for _ in range(t):
    m,n = map(int,sys.stdin.readline().split())
    graph = list()
    for _ in range(m):
        graph.append(list(map(int,sys.stdin.readline().split())))
    upper_graph.append(graph)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
        
queue = deque()
for g in upper_graph:
    n = len(g[0])
    m = len(g)
    k = (0,0)
    box = (0,0)
    visited = []
    for _ in range(m):
        visited.append([0] * n) 
    for i in range(m):
        for j in range(n):
            if g[i][j] == 3:
                queue.append((j,i))
                visited[j][i] = 1
            if g[i][j] == 4:
                k = (j,i)
            if g[i][j] == 2:
                box = (j,i)
    #bfs
    while queue:
        n_x,n_y = queue.popleft()
        
        for move in range(4):
            x = n_x + dx[move]
            y = n_y + dy[move]

            if 0 <= x < n and 0 <= y < m and visited[y][x] == 0 and g[y][x] != 1:
                queue.append((x,y))
                visited[y][x] = 1
    
 

    if visited[k[1]][k[0]] == 1 and visited[box[1]][box[0]] == 1:
        answer.append(1)
    else:
        answer.append(0)

for i in answer:
    print(i)