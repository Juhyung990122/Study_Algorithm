from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = list()
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx=  [0,0,-1,1]
dy = [-1,1,0,0]

queue = deque()
queue.append((0,0,0))
visited[0][0][0] = 1

while queue:
    now_y, now_x, crushed = queue.popleft()
    if now_y == n-1 and now_x == m-1:
        break
    for i in range(4):
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]

        if move_x < 0 or move_x > m-1 or move_y > n-1 or move_y < 0:
            continue

        # 벽인데 아직 안부순 경우 부수고 전진
        if graph[move_y][move_x] == 1 and crushed == 0 and visited[move_y][move_x][crushed + 1] == 0:
            visited[move_y][move_x][crushed + 1] = visited[now_y][now_x][crushed] + 1
            queue.append((move_y, move_x, crushed + 1))

        # 벽이 아니고 전에 방문한적 없으면 전진
        elif graph[move_y][move_x] == 0 and visited[move_y][move_x][crushed] == 0:
            visited[move_y][move_x][crushed] = visited[now_y][now_x][crushed] + 1
            queue.append((move_y, move_x, crushed))

if visited[n-1][m-1][crushed] == 0:
    print(-1)
else:
    print(visited[n-1][m-1][crushed])


