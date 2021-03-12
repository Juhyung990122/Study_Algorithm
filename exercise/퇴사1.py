import sys

n = int(sys.stdin.readline())
sc = list()
dp = [0] * n
for day in range(n):
    x,y = tuple(map(int,sys.stdin.readline().split()))
    sc.append((x,y))
    dp[day] = y

for i in range(n):
    # 오늘 + 작업일수가 n을 넘어가면 0으로 바꿔주고
    if i + sc[i][0] > n:
        dp[i] = 0
        continue
    #아니면 뒤에있는거 돌면서 맥스값으로 갱신
    for j in range(i+sc[i][0],n):
        dp[j] = max(dp[i]+sc[j][1],dp[j])
    
print(max(dp))


