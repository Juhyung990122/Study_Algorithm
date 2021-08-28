import sys

n = int(sys.stdin.readline())
date = list()
dp = [0] * n

for d in range(n):
    t, p = map(int,sys.stdin.readline().rstrip().split())
    date.append((t,p))

print(date,dp)
profit = 0
for i in range(n):
    print(i)
    profit = max(dp[i],profit)
    if i + date[i][0] > n:
        continue
    dp[i + date[i][0]] = max(profit+date[i][1],dp[i + date[i][0]])
    print(dp)