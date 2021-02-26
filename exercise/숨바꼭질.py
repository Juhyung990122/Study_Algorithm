from collections import deque

n,k = map(int,input().split())
visited = [False] * 501

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == k :
            print(visited[x])
            break
        for i in [x-1,x+1,x*2]:
            if 0 <= i <= 500 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

bfs(n)