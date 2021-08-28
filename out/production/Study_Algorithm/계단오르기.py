'''n = int(input())
stairs = list()
for _ in range(n):
    stairs.append(int(input()))

dp = list()

#초기값 설정
dp.append(stairs[0]) 
dp.append(max(stairs[0]+stairs[1], stairs[1]))
dp.append(max(stairs[2] + stairs[0], stairs[2] + stairs[1]))

for i in range(3,n):
    dp.append(max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2]))

print(dp[-1])
    '''

import sys
n = int(sys.stdin.readline())
cost = [0] * 300
for i in range(n):
    cost[i] = int(sys.stdin.readline())
#n번째 계단으로 가는 방법 두개(1칸 or 2칸) 중 가장 cost가 큰 애들 저장
dp =  [0] * 300

dp[0] = cost[0]
dp[1] = cost[0]+cost[1]
dp[2] = max(cost[2]+cost[1],cost[0]+cost[2])
        
for i in range(3,n):
    dp[i] = max(cost[i]+cost[i-1]+dp[i-3], cost[i]+dp[i-2])
print(dp[n-1])