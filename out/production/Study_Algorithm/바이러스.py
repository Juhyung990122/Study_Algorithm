'''
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
visited = [0] * n
answer = 0

graph = dict()
for i in range(1,n+1):
    graph[i] = list()

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

queue = []
queue.append(1)
visited[0] = 1
while queue:
    for i in graph[queue.pop(0)]:
        if visited[i-1] == 0:
            queue.append(i)
            answer += 1
            visited[i-1] = 1
        

print(answer)
'''
import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = dict()
for init in range(1,n+1):
    graph[init] = list()

for _ in range(m):
    c1,c2 = map(int,sys.stdin.readline().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
    
def bfs(start):
    answer = 0
    queue = deque()
    queue.append(start)
    visited = [1]+[0] * n
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in range(len(graph[now])):
            a_now = graph[now][i]
            if visited[a_now] == 0:
                queue.append(a_now)
                visited[a_now] = 1
                answer += 1
    return answer

print(bfs(1))