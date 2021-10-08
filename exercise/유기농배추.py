from collections import deque
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    answer = 0
    m,n,k = map(int,sys.stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i in range(k):
        x,y = map(int,sys.stdin.readline().split())
        field[y][x]=1


    dx = [-1,1,0,0]
    dy = [0,0,-1,1]    
    queue = deque()
    for y in range(n):   
        for x in range(m):
            if field[y][x] == 1:
                queue.append((y,x))
                field[y][x] = 0
                while queue:
                    p = queue.popleft()
                    for i in range(4):
                        move_y = p[0] + dy[i]
                        move_x = p[1] + dx[i]
                        if 0 <= move_y < n and 0<= move_x < m and field[move_y][move_x] == 1:
                            queue.append((move_y,move_x))
                            field[move_y][move_x] = 0
                answer += 1
    print(answer)



