'''
dp = [0]+[10001] * k

for i in range(n):
    for j in range(coin[i],k+1):
        dp[j] = min(dp[j],dp[j-coin[i]]+1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])
    '''
import sys
n,k = map(int,sys.stdin.readline().split())
coin = list()
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.sort()

dp = [100001] * (k+1)

for i in range(n):
    for j in range(k+1):
            dp[j] = min(dp[j],dp[j - coin[i]]+1)
    print(dp)

if dp[-1] == 100001:
    print(-1)
else:
    print(dp[-1])
