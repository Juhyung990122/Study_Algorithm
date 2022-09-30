import imp
import sys
from collections import deque

dy = [1,-1, 0, 0]
dx = [0, 0, 1, -1]

r, c = map(int, sys.stdin.readline().split())

graph = list()
for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

f_visited, j_visited = [[0] * c for _ in range(r)], [[0] * c for _ in range(r)]
f_queue, j_queue = deque(), deque()

for y in range(r):
    for x in range(c):
        if graph[y][x] == "F":
            f_queue.append((y, x))
            f_visited[y][x] = 1
        elif graph[y][x] == "J":
            j_queue.append((y, x))
            j_visited[y][x] = 1

def bfs_fire_and_Jihoon():
    # 불 먼저 돌림
    while f_queue:
        y, x = f_queue.popleft()
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            if 0 <= move_y < r and 0 <= move_x < c:
                if f_visited[move_y][move_x]  == 0 and graph[move_y][move_x] != "#":
                    f_visited[move_y][move_x] = f_visited[y][x] + 1
                    f_queue.append((move_y, move_x))

    # 지훈이 돌림
    while j_queue:
        y, x = j_queue.popleft()
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            if 0 <= move_y < r and 0 <= move_x < c:
                if j_visited[move_y][move_x]  == 0 and graph[move_y][move_x] != "#":
                    if f_visited[move_y][move_x] == 0 or f_visited[move_y][move_x] > j_visited[y][x] + 1:
                        j_visited[move_y][move_x] = j_visited[y][x] + 1
                        j_queue.append((move_y, move_x))

            else:
                return j_visited[y][x]

    return "IMPOSSIBLE"
            
print(bfs_fire_and_Jihoon())
