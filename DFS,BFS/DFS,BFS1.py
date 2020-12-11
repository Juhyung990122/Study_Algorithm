n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 범위 바깥
    if x < 0  or x >= n or y < 0 or y >= m:
        return False
    #범위 내 + xy 미방문
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상하좌우 확인 후 방문처리
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        # 힌 구역 스캔 끝
        return True
    #graph[x][y]가 1이면 이미 접근했거나 막혀있던 애니까 패스
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1
print(answer)


