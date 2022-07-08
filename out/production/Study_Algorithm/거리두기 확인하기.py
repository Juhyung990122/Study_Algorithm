from collections import deque
from os import popen

def bfs(graph):
    start = []
    for i in range(5):
        for j in range(5):
            if graph[i][j] == "P":
                start.append([i,j])
    
    for s in start:
        j = s[0]
        i = s[1]
        queue = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[j][i] = 1

        while queue:
            print(distance)
            y,x = queue.popleft()
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if graph[ny][nx] == "O":
                        queue.append([ny,nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if graph[ny][nx] == "P":
                        if distance[y][x] < 2:
                            return 0

    return 1



    return 

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))