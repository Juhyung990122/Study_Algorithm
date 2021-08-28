import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = list(list([-1]*m) for _ in range(n))

def dfs(col,row):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    if col == n-1 and row == m-1:
        return 1

    if dp[col][row] == -1 :
        dp[col][row] = 0
        for i in range(4):
            move_col = col + dy[i]
            move_row = row + dx[i]
            if 0 <= move_col < n and 0 <= move_row < m:
                if graph[col][row] > graph[move_col][move_row]:
                    dp[col][row] += dfs(move_col,move_row)
    return dp[col][row]
print(dfs(0,0))
                    



            

