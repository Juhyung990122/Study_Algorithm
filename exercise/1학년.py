import sys

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

dp = [[0] * 20 for _ in range(n)]
dp[0][num_list[0]] = 1

for i in range(1,n):
    for j in range(20):
        if j - num_list[i] >= 0:
            if dp[i-1][j - num_list[i]] != 0:
                dp[i][j] += dp[i-1][j]
        if j + num_list[i] < 20:
            if dp[i-1][j + num_list[i]] != 0:
                dp[i][j] += dp[-1][j]
print(dp)


