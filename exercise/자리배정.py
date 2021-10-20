c,r = map(int,input().split())
k = int(input())

seat = [[0] * r for _ in range(c)]

# x축 증가  y축 증가 x축 감소, y축 감소
dir = [[0,1],[1,0],[0,-1],[-1,0]]

y,x = 0,-1
d = 0
now = 1

if k > c*r:
    print(0)
else:
    while now <= k:
        move_y = y + dir[d][0]
        move_x = x + dir[d][1]

        if move_y < 0 or c <= move_y:
            d = (d + 1) % 4
            continue
        if move_x < 0 or r <= move_x:
            d = (d + 1) % 4
            continue
        if seat[move_y][move_x] != 0 :
            d = (d + 1) % 4
            continue

        if now == k:
            print(move_y+1,move_x+1)

        seat[move_y][move_x] = now
        now += 1
        y,x = move_y,move_x

