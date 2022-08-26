def solution(rows, columns, queries):
    answer = []
    # graph = [[0] * rows for _ in range(columns)]

    # num = 1
    # for i in range(columns):
    #     for j in range(rows):
    #         graph[i][j] = num
    #         num += 1
    graph =  [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    for x1,y1,x2,y2 in queries:
        top,left,bottom,right = x1-1,y1-1,x2-1,y2-1
        temp = graph[top][left]
        min = temp

        for y in range(top,bottom):
            value = graph[y+1][left]
            graph[y][left] = value
            if min > graph[y+1][left]:
                min = graph[y+1][left]

        for x in range(left,right):
            graph[bottom][x] = graph[bottom][x+1]
            if min > graph[bottom][x+1]:
                min = graph[bottom][x+1]

        for y in range(bottom,top,-1):
            graph[y][right] = graph[y-1][right]
            if min > graph[y-1][right]:
                min = graph[y-1][right]

        for x in range(right,left,-1):
            graph[top][x] = graph[top][x-1]
            if min > graph[top][x-1]:
                min = graph[top][x-1]
        
        graph[top][left+1] = temp 
        answer.append(min)
    
    return answer

print(solution(100,97,[[1,1,100,97]]))