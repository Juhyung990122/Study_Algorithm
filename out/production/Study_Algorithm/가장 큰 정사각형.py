import sys

n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
size = 0
for i in range(1,n):
    for j in range(1,m):
        if graph[i][j] != 0:
            s = graph[i][j-1]
            d = graph[i-1][j]
            ds = graph[i-1][j-1]
            graph[i][j] = max(min(s,d,ds) + 1,graph[i][j])
            if size < graph[i][j]:
                size = graph[i][j]
if n == 1 or m == 1:
    size = 1
print(size ** 2)