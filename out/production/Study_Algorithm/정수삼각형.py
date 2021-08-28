import sys
n = int(sys.stdin.readline())
graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


for list_idx in range(1,n):
    for line_idx in range(list_idx+1):
        if line_idx == 0:
            graph[list_idx][line_idx] += graph[list_idx-1][line_idx]
            continue
        if line_idx == len(graph[list_idx])-1:
            graph[list_idx][line_idx] += graph[list_idx-1][line_idx-1]
            continue
        graph[list_idx][line_idx] += max(graph[list_idx-1][line_idx-1], graph[list_idx-1][line_idx])

print(max(graph[-1]))
        
        





