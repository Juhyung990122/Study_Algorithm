def solution(n):
    dir = [[1,0],[0,1],[-1,-1]]
    triangle = [[0] * i for i in range(1,n+1)]
    a = sum(i for i in range(1,n+1))

    y,x = -1,0
    d = 0
    now = 1

    while now <= a:
        move_y = y + dir[d][0]
        move_x = x + dir[d][1]
        if move_y < 0 or n <= move_y:
            d = (d + 1)%3
            continue
        
        if move_x < 0 or len(triangle[move_y]) <= move_x:
            d = (d + 1)%3
            continue
        
        if triangle[move_y][move_x] == 0:
            triangle[move_y][move_x] = now
            y,x = move_y,move_x
            now += 1
        
        else:
            d = (d + 1 ) % 3

    return sum(triangle,[])

print(solution(5))