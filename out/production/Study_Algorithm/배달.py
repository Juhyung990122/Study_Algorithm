from math import inf
from collections import deque
def solution(N, road, K):
    visited = [False] * (N+1)
    dists = [inf] * (N+1)
    dists[1] = 0
    queue = deque([1])
    answer = 0
    while queue:
        parent = queue.popleft()
        visited[parent] = True
        for start,end,dist in road:
            if start == parent or end == parent:
                target = start
                if start == parent:
                    target = end
                if dists[target] > dists[parent] + dist:
                    dists[target] = dists[parent] + dist
                    queue.append(target)
        
    for d in dists:
        if d <= K:
            answer += 1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))