#복습
'''
from collections import deque

def dfs(array,start,visited):
    visited[start] = True
    print(start)
    for i in array[start]:
        if not visited[i]:
            dfs(array,i,visited)

def bfs(array,start,visited):
    queue = deque([start])
    visited[start] = True
    print(start)
    for i in array[start]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

'''

# 미로탈출
from collections import deque

n,m = map(int,input().split(' '))
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

dx = [-1,1,0,0] #상하
dy = [0,0,-1,1] #좌우

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        #상하좌우 검색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n  or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                # 옮겨갈 좌표에 이동거리기록
                maze[nx][ny] = maze[x][y] + 1
                # 새로운 출발점(이동한 지점) 등록 + 이동지점 기준 탐색
                queue.append((nx,ny))
    #도착지에서 누적된 거리 리
    return maze[n-1][m-1]

print(bfs(0,0))

