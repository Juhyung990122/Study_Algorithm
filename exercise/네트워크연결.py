import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

cost = list()
for _ in range(m):
    a,b,c = list(map(int,sys.stdin.readline().split()))
    cost.append([a,b,c])

cost.sort(key=lambda x : x[2])
def find(x,parent):
    if x != parent[x]:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a = find(parent[a],parent)
    b = find(parent[b],parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [r for r in range(n+1)]
answer = 0

for i in range(len(cost)):
    if find(cost[i][0],parent) != find(cost[i][1],parent):
        union(cost[i][0],cost[i][1],parent)
        answer += cost[i][2]
print(answer)