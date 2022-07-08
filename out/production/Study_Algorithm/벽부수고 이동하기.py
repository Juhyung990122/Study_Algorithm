from collections import deque
n,m = map(int,input().split())
graph = list()
for i in range(n):
    graph.append(list(map(int,input())))

dx=  [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append([0,0,1])