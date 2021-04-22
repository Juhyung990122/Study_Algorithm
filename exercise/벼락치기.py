import sys

n,t = map(int,sys.stdin.readline().split())
sub = list()
for _ in range(n):
    sub.append(list(map(int,sys.stdin.readline().split())))

dp = ([0] * (k+1) for i in range(n))
time_list = list()

for index in range(n):
    dp[sub[index][0]] = sub[index][1]
    time_list.append(sub[index][0])

for i in range(sub[0][0],t+1):
    if i in time_list:
        now = i
        dp[i] = max(dp[i-1] ,dp[i])
        continue
    dp[i] = max(dp[i-1] ,dp[now] + dp[i-now])
print(dp)
# 이러면 1번 3번 선택했을때가 안된다..;ㅅ; 
print(dp[t])

