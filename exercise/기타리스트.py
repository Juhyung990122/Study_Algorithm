import sys

n,s,m = map(int,sys.stdin.readline().split())
dp = list()
v = list(map(int,sys.stdin.readline().split()))

for _ in range(n+1):
    dp.append([False] * (m + 1))

dp[0][s] = True
for i in range(1,n+1):
    for j in range(m+1):
        # 더할때
        if j - v[i-1] >= 0: 
            if dp[i-1][j-v[i-1]] == True:
                dp[i][j] = True
        # 뺄떄
        if j + v[i-1] <= m:
            if dp[i-1][j+v[i-1]] == True:
                dp[i][j] = True
answer = -1
for a in range(m,-1,-1):
    if dp[-1][a] == True:
        answer = a
        break
print(answer)
    




