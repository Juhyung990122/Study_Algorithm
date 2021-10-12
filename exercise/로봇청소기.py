n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 상 우 하 좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

y,x = r,c
head = d
answer = 1
graph[y][x] = 2

while True:
    visited = False
    print(graph)
    for i in range(4):
        head = (head - 1) % 4
        move_y = y + dy[head]
        move_x = x + dx[head]
        if move_y < 0 or n <= move_y or move_x < 0 or m <= move_x:
            continue
        
        if graph[move_y][move_x] == 0:
            answer += 1
            graph[move_y][move_x] = 2
            y = move_y
            x = move_x
            visited = True
            break

    # 네군데 다 방문했는데 청소할 곳 없으면
    if not visited:
        move_y = y - dy[head]
        move_x = x - dx[head]
        if move_y < 0 or n <= move_y or move_x < 0 or m <= move_x:
            print(answer)
            break
        else:
            if graph[move_y][move_x] == 2:
                x = move_x
                y = move_y
            elif graph[move_y][move_x] == 1:
                print(answer)
                break
