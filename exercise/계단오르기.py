n = int(input())
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
    
