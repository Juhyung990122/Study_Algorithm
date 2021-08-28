import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

dp = [1] * (n)
for i in range(len(num)):
    for j in range(i,n):
        if num[i] > num[j]:
            dp[j] = max(dp[i]+1,dp[j])

print(max(dp))