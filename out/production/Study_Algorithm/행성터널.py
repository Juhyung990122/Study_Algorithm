import sys

n = int(sys.stdin.readline())
planets = list()
for p in range(n):
    planets.append(list(map(int,sys.stdin.readline().split()))+[p])

planets.sort()
distance = list()
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1,n):
        distance.append((abs(planets[j-1][i] - planets[j][i]),planets[j-1][3],planets[j][3]))
distance.sort()
parent = [i for i in range(n)]
answer = 0

def find(x,parent):
    if x != parent[x]:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
answer = 0
for i in range(len(distance)):
    if find(distance[i][1],parent) != find(distance[i][2],parent):
        union(distance[i][1],distance[i][2],parent)
        answer += distance[i][0]
print(answer)