from collections import deque

n,m = map(int,input().split())
graph = list()
for _ in range(n): 
    graph.append(list(map(int,input())))

visited = [[0] * m for i in range(n)]
queue = deque()
queue.append([0,0])
visited[0][0] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

while queue:
    y,x = queue.popleft()
    if y == n-1 and x == m-1:
        print(visited[n-1][m-1])
        break

    for i in range(4):
        move_y = y + dy[i]
        move_x = x + dx[i]
        if 0 > move_y or move_y >= n or 0 > move_x or move_x >= m:
            continue
        if visited[move_y][move_x] == 0 and graph[move_y][move_x] == 1:
            queue.append([move_y,move_x])
            visited[move_y][move_x] = visited[y][x] + 1