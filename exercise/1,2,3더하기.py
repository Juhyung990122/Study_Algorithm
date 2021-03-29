import sys 
'''
t = int(sys.stdin.readline())
num = list()
for _ in range(t):
    num.append(int(sys.stdin.readline()))

dp = [0,1,2,4] + [0]* 8
for i in range(4,max(num)+1):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

for j in num:
    print(dp[j])
'''
#1,2,3 더하기 복습    
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp = [0,1,2,4]+[0] * (n-3)

    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1] 
    
    print(dp[-1])

    

