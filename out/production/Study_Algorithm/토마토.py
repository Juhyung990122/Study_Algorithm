from collections import deque
import sys
m,n = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#bfs를 사용할 것이므로 큐 사용
#큐 사용할때는 꼭 deque사용할 것 : pop에서 시간차이 많이남
queue = deque()

dx = [1, -1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

while queue:
    i,j = queue.popleft()
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
            graph[x][y] = graph[i][j] + 1
            queue.append([x,y])


possible = True
max_day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            possible = False
            break
        if graph[i][j] == -1:
            continue
        max_day = max(max_day,graph[i][j])
        

if possible == False:
    print(-1)

elif max_day == 1:
    print(0)

else:
    print(max_day - 1)


