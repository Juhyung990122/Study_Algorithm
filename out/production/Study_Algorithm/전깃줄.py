n = int(input())
line = list()
for i in range(n):
    line.append(list(map(int,input().split())))

dp = [1]+[0] * n
line.sort(key=lambda x :x[0])
for i in range(1,len(line)):
    dp[i] = 1
    for j in range(i):
        if line[i][1] > line[j][1] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
print(n-max(dp)) 
    