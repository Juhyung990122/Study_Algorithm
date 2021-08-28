n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

home_num = []
def dfs(x,y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

answer = 0
count = 0
home = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) != False:
            answer += 1
            home.append(len(home_num))
            home_num = []
            
print(answer)
home.sort()
for i in home:
    print(i)