import itertools
from collections import deque
import copy
def bfs(g,num):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    r_graph = g.copy()
    for i in range(n):
        for j in range(m):
            if g[i][j] == num:
                queue.append((i,j))
                visited[i][j] = 1
                while queue:
                    y,x = queue.pop()
                    for k in range(4):
                        move_y = y + dy[k]
                        move_x = x + dx[k]
                        if 0 > move_y or move_y >= n or 0 > move_x or move_x >= m:
                            continue
                        if g[move_y][move_x] == 0 and visited[move_y][move_x] == 0:
                            queue.append([move_y,move_x])
                            visited[move_y][move_x] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                r_graph[i][j] = num
    return r_graph,visited


global n,m

n,m = map(int,input().split())


graph = list()
for _ in range(n):
    graph.append(list(map(int,input().split())))

empty = list()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append([i,j])


empty = list(itertools.permutations(empty,3))
max = 0
for i in range(len(empty)):

    safe_zone = 0
    g_copy = copy.deepcopy(graph)

    wall = empty[i]

    for j in range(3):
        g_copy[wall[j][0]][wall[j][1]] = 1

    virus,v = bfs(g_copy,2)

    safe,s = bfs(virus,0)
    for a in range(n):
        for b in range(m):
            if s[a][b] == 1:
                safe_zone += 1
    if safe_zone > max:
        max = safe_zone



print(max) 