import sys

n,k = map(int,sys.stdin.readline().split())

answer = 0
dp = [[0] * (n+1) for _ in range(k)]
dp[0] = [1] * (n+1)

for row in range(1, k):
    for col in range(n+1):
        for j in range(col+1):
            dp[row][col] += dp[row-1][j]
            
print(dp[k-1][-1])
           
            