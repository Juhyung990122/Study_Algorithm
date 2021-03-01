import sys

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
