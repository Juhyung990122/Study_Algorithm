import sys

n = int(sys.stdin.readline())
answer = 0
dp = list([0] * 10 for _ in range(n+1))
for k in range(1,10):
    dp[1][k] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
            continue
        if j == 9:
            dp[i][j] = dp[i-1][8]
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = 0 
for a in dp[n]:
    answer += a
print(answer % 1000000000)