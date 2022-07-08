def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)]
    r,c = 0,0
    next_r,next_c = 0,0
    graph[r][c] = 1
    write_num = 1
    zero  = rows * columns - 1

    while True:

        # move 
        if write_num % 2 == 0:
            next_r = r + 1
            if next_r == rows:
                next_r = 0
        else:
            next_c = c + 1
            if next_c == columns:
                next_c = 0


        #break
        if graph[next_r][next_c] != 0:
            if graph[next_r][next_c] % 2 == 0:
                if (write_num + 1) % 2 == 0:
                    break
            else:
                if (write_num + 1) % 2 == 1:
                    break
        
        if zero == 0:
            break
        
        r = next_r
        c = next_c

        if graph[r][c] == 0:
            zero -= 1
        
        graph[r][c] = write_num + 1
        write_num = graph[r][c]


    return graph
print(solution(3,4))
print(solution(3,3))