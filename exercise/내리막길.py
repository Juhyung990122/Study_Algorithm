import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

queue = deque()
queue.append((0,0))
visited = list(list([0]*m) for _ in range(n))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
height = graph[0][0]

while queue:
    now = queue.pop()
    height = graph[now[0]][now[1]]
    for k in range(4):
        move_r = now[1] + dx[k]
        move_c = now[0] + dy[k]
        if 0 <= move_r < m and 0 <= move_c < n and visited[move_c][move_r] == 0 and height > graph[move_c][move_r]:
            queue.append((move_c,move_r))
            visited[move_c][move_r] += 1
    
    if visited[n-1][m-1] == 1:
        answer += 1
        visited = list(list([0]*m) for _ in range(n))

print(answer)
                
                    



            

