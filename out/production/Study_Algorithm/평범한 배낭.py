import sys

n,k = map(int,sys.stdin.readline().split())
obj_list = list()

for _ in range(n):
    obj_list.append(list(map(int,sys.stdin.readline().split())))

dp = [[0] * (k+1) for _ in range(n)]
# 가치합 = i번째 물건을 넣었을때 최대 가치
for i in range(len(obj_list)):
    w,v = obj_list[i]
    for j in range(k+1):
        if w <= j:
            dp[i][j] = max(v + dp[i-1][j - w],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[-1]))