from collections import deque


n = int(input())
k = int(input())

graph = [[0]* n for _ in range(n)]

for _ in range(k):
    y,x = map(int,input().split())
    graph[y-1][x-1] = 1

l = int(input())
dirs_change = {}
for _ in range(l):
    x,c = list(input().split())
    dirs_change[int(x)] = c

# 상 좌 하 우
dy = [-1,0,1,0]
dx = [0,-1,0,1]

time = 0
x,y = 0,0
head = 3
snake = deque([[0,0]])

while True:
    
    time += 1 
    move_y = y + dy[head]
    move_x = x + dx[head]

    if move_y < 0  or move_y >= n or move_x < 0 or move_x >= n:
        break
    # 여기 논리오류 났었음 
    if [move_y,move_x] in snake:
        break
    
    snake.append([move_y,move_x])
    if graph[move_y][move_x] == 1:
        graph[move_y][move_x] = 0
    else:
        snake.popleft()
    # 갱신 꼭 해줄 것
    y,x = move_y, move_x
    
    # 여기 외우기ㅋㅋㅋ 
    if time in dirs_change.keys():
        if dirs_change[time] == "L":
            head = (head + 1)%4
        else:
            head = (head + 3)%4
    

print(time)
