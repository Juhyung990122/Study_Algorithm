import sys

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

dp = [[0] * 21 for _ in range(n-1)]
dp[0][num_list[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            if j - num_list[i] >= 0:
                dp[i][j - num_list[i]] += dp[i-1][j]
            if j + num_list[i] <= 20:
                dp[i][j + num_list[i]] += dp[i-1][j]
                
                
print(dp[-1][num_list[-1]])


