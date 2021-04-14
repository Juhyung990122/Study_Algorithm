import sys
from collections import deque
n,q = map(int,sys.stdin.readline().split())
graph = dict()

def find(k,v,graph):
    queue = deque()
    queue.append((v,float('inf')))
    visited = [-1]+[0] * n
    visited[v] = 1
    count = 0

    while queue:
        v1, now_cost = queue.pop()
        for v2, cost in graph[v1]:
            if visited[v2] == 1:
                continue
            # k보다 크면 쭉 따라서 연결된애들중에 큰거 있는지 또 확인확인
            if cost >= k:
                count += 1
                #now_cost 랑 cost중 작은애로 갱신시켜서 queue에 집어넣어주기. 사실 안해도 딱히 상관없긴해...
                if now_cost > cost:
                    queue.append((v2,cost))
                else:
                    queue.append((v2,now_cost))
                visited[v2] = 1   
    return count

for i in range(1,n+1):
    graph[i] = list()
for _ in range(n-1):
    v1, v2, cost = map(int,sys.stdin.readline().split())
    graph[v1].append([v2,cost])
    graph[v2].append([v1,cost])

    
answer = list()
for _ in range(q):
    k,v = map(int,sys.stdin.readline().split())
    answer.append(find(k,v,graph))

for i in answer:
    print(i)

