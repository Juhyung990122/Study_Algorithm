n = int(input())
graph = list()
for i in range(n):
    graph.append(list(map(int,input())))

def divide(x,y,n):
    if n == 1:
        print(graph[y][x],end = "")
        return
    # 같다면 트루
    flag = True

    for i in range(y,y+n):
        for j in range(x,x+n):
            if graph[i][j] != graph[y][x]:
                flag = False
                break
        
    if flag:
        print(graph[y][x], end= "")
    else:
        d_n = n // 2

        print("(", end = "")
        divide(x,y,d_n)
        divide(x+d_n,y,d_n)
        divide(x,y+d_n,d_n)
        divide(x+d_n,y+d_n,d_n)
        print(")",end="")

divide(0,0,n)

