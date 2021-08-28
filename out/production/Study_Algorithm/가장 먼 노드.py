from collections import deque

def solution(n, edge):
    answer = 0
    graph = dict()
    dist = [0] * (n+1)

    for i in range(1,n+1):
        graph[i] = list()

    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
        
    queue = deque([1])

    while queue:
        now = queue.popleft()
        for i in range(len(graph[now])):
            if graph[now][i] == 1:
                continue
            if dist[graph[now][i]] != 0:
                if dist[graph[now][i]] <= dist[now] + 1:
                    continue
                else:
                    queue.append(graph[now][i])
                    dist[graph[now][i]] = dist[now] + 1

            else:
                queue.append(graph[now][i])
                dist[graph[now][i]] = dist[now] + 1
    
    max_dist = max(dist)
    answer = dist.count(max_dist)
    
    return answer

print(solution(2, [[1, 2]]))