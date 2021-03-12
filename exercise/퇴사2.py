import sys
n = int(sys.stdin.readline())
sc = list()
dp = [0] * n

for day in range(n):
    x,y = tuple(map(int,sys.stdin.readline().split()))
    sc.append((x,y))

profit = 0
for i in range(n):
    # 현재까지의 이익
    profit = max(profit,dp[i])
    #날짜 넘어가면 패스
    if i + sc[i][0] > n:
        continue
    # 오늘을 기점으로 그일을 할까 말까 결정
    # 할거면 현재이익 + 지금일해서 얻는 이익, 안할거면 그냥 그대로 두고 넘어가기
    dp[i + sc[i][0]] = max(profit+sc[i][1],dp[i+sc[i][0]])
    
print(max(dp))

