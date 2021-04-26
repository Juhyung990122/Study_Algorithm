import sys
import heapq

INF = 1e15
n,p,k = map(int,sys.stdin.readline().split())
graph = dict()
for i in range(1,n+1):
    graph[i] = list()

for _ in range(p):
    x,y,c = map(int,sys.stdin.readline().split())
    graph[x].append((y,c))
    graph[y].append((x,c))

print(graph)
distance = [0]+[INF] * (n)
queue = []
heapq.heappush(queue,(1,0))
distance[1] = 0
while queue:
    start,cost = heapq.heappop(queue)
    #이미 최소값이라면 패스
    if distance[start] < cost:
        continue
    for v2,cost in graph[start]:
        d = distance[start] + cost
        if d < distance[v2]:
            distance[v2] = d
            heapq.heappush(queue,(v2,d))
            print(distance)
            print(queue)



    
