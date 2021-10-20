n = int(input())
d = list()
for _ in range(n):
    d.append(list(map(int,input().split())))

d.sort(key = lambda x : (x[1],x[0]))

for y,x in d:
    print(y,x)

