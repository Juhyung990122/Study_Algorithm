import sys
'''
n = int(sys.stdin.readline())
#dp에는 방법 수 저장
dp = [0] * 1001


dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    #마지막칸 2*1 2개로 채우기 or 1*2 로 채우기로 방법이 나뉘어짐
    #dp[n] = dp[n-2] + dp[n-1]
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[n])
'''

def solution(n):
    answer = 0
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] =(dp[i-2] + dp[i-1]) % 1000000007
    
    answer = dp[-1] 
    return answer

print(solution(10))