import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1

# 2칸일때 1칸짜리랑 안겹치는거 3개
# 4칸부터는 이전애들이랑 안겹치는거 2개씩 나옴
for i in range(2,n+1,2):
    #2칸짜리 활용할거니까 2칸전꺼 * 2칸짜리(3개)
    dp[i] = dp[i-2] * 3
    #4칸짜리 활용할거부터는 2개씩 
    for j in range(i-4,-1,-2):
        dp[i] += dp[j] * 2
print(dp[-1])