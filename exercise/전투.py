import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(m):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color):
    visited = []
    for _ in range(m):
        visited.append([0]*n)
    queue = deque()
    my_team = 0
    opnt_team = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                queue.append((i,j))
                visited[i][j] = 1
                count = 0
                while queue:
                    move_y,move_x = queue.popleft()
                    count += 1
                    for k in range(4):
                        x = move_x + dx[k]
                        y = move_y + dy[k]
                        if 0 <= x < n and 0 <= y < m and visited[y][x] == 0 and graph[y][x] == color:
                            queue.append((y,x))
                            visited[y][x] = 1 
                my_team += count ** 2
    return my_team

print(bfs('W'),bfs('B'))
