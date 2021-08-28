import sys
from collections import deque
t = int(sys.stdin.readline())
answer = list()
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())  
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1

    queue = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))
                graph[i][j] = 0
                while queue:
                    now = queue.popleft()
                    for idx in range(4):
                        move_y= now[0] + dy[idx]
                        move_x = now[1] + dx[idx]
                        if 0 <= move_x < m and 0 <= move_y < n and graph[move_y][move_x] == 1:
                            queue.append((move_y,move_x))
                            graph[move_y][move_x] = 0
                count += 1
    answer.append(count)
for k in answer:
    print(k)