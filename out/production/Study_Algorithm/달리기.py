import sys
from collections import deque
import math 
n,m,k = map(int,sys.stdin.readline().split())
graph = list()
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
x1 = x1 - 1
y1 = y1 - 1
x2 = x2 - 1
y2 = y2 - 1


dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
queue.append([x1,y1])
visited[x1][y1] = 0
answer = 0
while queue:
    now = queue.popleft()
    if now[0] == x2 and now[1] == y2:
        break
    for i in range(4):
        for j in range(1,k+1):
            r = dx[i] * j + now[0]
            c = dy[i] * j + now[1]
            if 0 <= r < n and 0 <= c < m and graph[r][c] != '#':
                if visited[r][c] == 0:
                    queue.append([r,c])
                    visited[r][c] = visited[now[0]][now[1]] + 1
                elif visited[r][c] == visited[now[0]][now[1]] + 1:
                        continue
            else:
                break
    
    
if visited[x2][y2] == 0:
    print(-1)
else:
    print(visited[x2][y2])



