
def out(y,x,d,grid,dir):
    ny = y + dir[d][0]
    nx = x + dir[d][1]

    if ny >= len(grid):
        ny = 0
    elif ny < 0:
        ny = len(grid)-1
    if nx >= len(grid[0]):
        nx = 0
    elif nx < 0:
        nx = len(grid[0])-1
    return ny,nx

def dfs(state,origin,route,grid):
    dir = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    y = state[0]
    x = state[1]
    d = state[2]
    visited[d][y][x] = 1
    
    ny,nx = out(y,x,d,grid,dir)
    value = grid[ny][nx]

    if value == "R":
        d = (d+5)%4
    elif value == "L":
        d = (d+7)%4

    if origin[0] == ny and origin[1] == nx and origin[2] == d:
        answer.append(route)
        return

    if not visited[d][ny][nx]:
        dfs([ny,nx,d],origin,route+1,grid)

def solution(grid):
    global answer,visited
    answer = []
    n = len(grid)
    m = len(grid[0])
    visited = [[[0]*m for _ in range(n)] for _ in range(4)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                dfs([i,j,k],[i,j,k],1,grid)
    return answer
print(solution(["SL","LR"]))