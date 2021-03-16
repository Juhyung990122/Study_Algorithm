import sys
n = int(sys.stdin.readline())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

print(graph)
start = (0,0)
end = (n-1,n-1)
answer = 0
print("[0]", start, end)
while (end[0] - start[0]+1) *  (end[1]-start[1]+1) > 1 :
    #가로1
    max_case = 1
    max_total = 0
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    height = (end[0]-start[0] + 1)
    width = (end[1]-start[1] + 1)
    if height != 1:
        for i in range(start[0], start[0]+height//2):
            for j in range(start[1],start[1]+width):
                if m1 < graph[i][j]:
                    m1 = graph[i][j]
        if max_total < m1:
            max_case = 1
            max_total = m1
    #가로2
        for i in range(start[0]+height//2,start[0]+height):
            for j in range(start[1],start[1]+width):
                if m2 < graph[i][j]:
                    m2 = graph[i][j]
        if max_total < m2:
            max_case = 2
            max_total = m2   
    if width != 1:         
    #세로1
        for i in range(start[0],start[0]+height ):
            for j in range(start[1],start[1]+width//2):
                if m3 < graph[i][j]:
                    m3 = graph[i][j]
        if max_total < m3:
            max_case = 3
            max_total = m3
        #세로2
        for i in range(start[0],start[0]+height):
            for j in range(start[1]+width//2,start[1]+width):
                if m4 < graph[i][j]:
                    m4 = graph[i][j]
        if max_total < m4:
            max_case = 4
            max_total = m4
    print("[1]", start, end)
    answer += max_total
    #max_case1 이면 2로 덮고
    if max_case == 1:
        nstart = (start[0]+height//2 ,start[1])
        nend = (start[0]+height-1 ,start[1]+width -1)
    # 2면 1
    if max_case == 2:
        nstart = (start[0],start[1])
        nend = (start[0]+height//2-1,start[1]+width-1)
    # 3이면 4
    if max_case == 3:
        nstart = (start[0],start[1]+width//2)
        nend = (start[0]+height -1,start[1]+width -1)
    # 4면 3 
    if max_case == 4:
        nstart = (start[0],start[1])
        nend = (start[0]+height -1,start[1]+width//2-1)
    start = nstart
    end = nend
    print(max_case)
    print('t:',start,end)
    
print(answer)