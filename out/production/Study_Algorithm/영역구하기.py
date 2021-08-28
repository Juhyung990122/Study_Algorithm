import sys
from collections import deque
m,n,k = map(int,sys.stdin.readline().split())
graph = list([0]*n for _ in range(m))
rec = list()

for _ in range(k):
    rec.append(list(map(int,sys.stdin.readline().split())))

for loca in rec:
    for c in range(loca[0],loca[2]): #세로
        for r in range(m-loca[3],m-loca[1]): #가로
            graph[r][c] = -1

answers = list()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(m): #세로
    for j in range(n): #가로
        if graph[i][j] == 0 :
            queue = deque()
            queue.append((i,j))
            graph[i][j] = 1
            answer = 1
            while queue:
                x,y = queue.popleft()
                for d in range(4):
                    move_x = x + dx[d]
                    move_y = y + dy[d]
                    if 0 <= move_x < m and 0 <= move_y < n:
                        if graph[move_x][move_y] == 0:
                            answer += 1
                            graph[move_x][move_y] = 1
                            queue.append((move_x,move_y))
            answers.append(answer)

print(len(answers))
answers.sort()
for i in answers:
    print(i,end = ' ')
