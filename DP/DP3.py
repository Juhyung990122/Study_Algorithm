#바닥 공사
n = int(input())

d = [0]*1001

#점화식 == ai = ai-1 + ai-2*2
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i]+d[i-1]*2) % 796796
print(d[n])