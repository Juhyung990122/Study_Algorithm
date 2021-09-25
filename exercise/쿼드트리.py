n = int(input())
graph = list()
for i in range(n):
    graph.append(list(map(int,input())))

def qt(x,y,n):
    if n == 1:
        print(graph[y][x],end="")
        return
    same = True
    for i in range(y,y+n):
        for j in range(x,x+n):
            if graph[i][j] != graph[y][x]:
                same = False
                break
    
    if same == True:
        print(graph[y][x],end="")
    else:
        print("(",end="")
        n //= 2
        qt(x,y,n)
        qt(x+n,y,n)
        qt(x,y+n,n)
        qt(x+n,y+n,n)
        print(")",end="")

qt(0,0,n)