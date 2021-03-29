import sys
'''
n = int(sys.stdin.readline())
answer = 0

d = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        continue
    n = []
    n.append(d[i-1] + 1)
    if i % 3 == 0:
        n.append(d[i//3] + 1) 
    if i % 2 == 0:
        n.append(d[i//2] + 1)
    d[i]= min(n)
    

print(d[i])
'''
n = int(sys.stdin.readline())
count = 0
dp = [0] * (n+1) #연산횟수 저장, 각 인덱스가 계산하는 숫자.
for i in range(1,n+1):
    if i == 1:
        continue
    
    # 1,2,3 의 경우들중 가장 카운트 작은걸로 저장.
    dp[i] = dp[i-1] +1 
    if i % 3 == 0:
        dp[i] = min(dp[i // 3]+1 , dp[i]) 
        
    if i % 2 == 0:
        dp[i] = min(dp[i // 2]+1, dp[i])


print(dp[-1])