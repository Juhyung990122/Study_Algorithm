import sys
n,k = map(int,sys.stdin.readline().split())
coin = list()
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

dp = [0]+[10001] * k

for i in range(n):
    for j in range(coin[i],k+1):
        dp[j] = min(dp[j],dp[j-coin[i]]+1)

print(dp)