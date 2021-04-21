from collections import deque
def solution(N, road, K):
    answer = 0
    graph = dict()
    for i in range(len(road)):
        graph[i+1] = list()
    for v1,v2,cost in road:
        graph[v1].append([v2,cost])
        graph[v2].append([v1,cost])
    cost_list = { i:float('inf') if i != 1 else 0 for i in range(1, N+1) }
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for v2,cost in graph[now]:
            if cost_list[v2] > cost_list[now] + cost:
                cost_list[v2] = cost_list[now] + cost
                queue.append(v2)

    for i in cost_list.values():
        if i <= K:
            answer += 1
    return answer

print(solution(	6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))