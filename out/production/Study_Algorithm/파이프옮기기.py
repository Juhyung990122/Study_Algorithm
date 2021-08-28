import sys

n = int(sys.stdin.readline())
graph = list()
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 가 0, 세 1, 대 2
x = 0
y = 1
now = 0

def dfs(x,y,now):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return 

    # 가로나 대각선이면
    if now == 0 or now == 2:
        if y + 1 < n:
            if graph[x][y+1] == 0:
                # 가로
                dfs(x,y+1,0)
    
    # 세로나 대각선이면
    if now == 1 or now == 2:
        if x + 1 < n:
            if graph[x+1][y] == 0:
                #세로
                dfs(x+1,y,1)
    
    # 대각선이면
    if now == 0 or now == 1 or now == 2:
        if x+1 < n and y+1 < n:
            if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0 :
                dfs(x+1,y+1,2)
answer = 0
dfs(x,y,now)
print(answer)
    
