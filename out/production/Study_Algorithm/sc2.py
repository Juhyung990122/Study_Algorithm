from collections import deque
from math import inf 
def solution(N, road, K):
    answer = 0

    cost_list = [inf] * (N+1)
    visited = [False] * (N+1)
    cost_list[1] = 0
    queue = deque([1])
    while queue:
        now = queue.popleft()
        visited[now] = True
        for v1,v2,cost in road:
            if now == v1 or now == v2:
                target = v1
                if v1 == now:
                    target = v2
                if cost_list[target] > cost_list[now] + cost:
                    cost_list[target] = cost_list[now] + cost
                    queue.append(target) 

    for i in cost_list:
        if i <= K:
            answer += 1
    return answer

print(solution(	6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))