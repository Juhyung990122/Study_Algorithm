import sys

n,t = map(int,sys.stdin.readline().split())
sub = list()
for _ in range(n):
    sub.append(list(sys.stdin.readline().split()))

dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(t+1):
        if j < sub[i-1][0]:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j - sub[i-1][0]]+sub[i-1][1])
print(dp[-1][-1])

