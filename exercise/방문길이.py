def solution(dirs):
    road = set()
    
    move_list = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    x,y = (0,0)
    
    for m in dirs:
        n_x,n_y = x + move_list[m][0], y + move_list[m][1]
        if -5 <= n_x <= 5 and -5 <= n_y <= 5:
            road.add((x,y,n_x,n_y)) 
            road.add((n_x,n_y,x,y))
            x,y = n_x, n_y

    answer = len(road) // 2