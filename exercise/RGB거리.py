import sys
n = int(sys.stdin.readline())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dp = [[-1] * 3 for _ in range(n)]
for i in range(3):
    dp[0][i] = graph[0][i]

for i in range(1, len(graph)):
    dp[i][0] = graph[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = graph[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = graph[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[-1]))