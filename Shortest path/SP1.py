#다익스트라 구현하기
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수
n,m = map(int,input().split())
# 시작점
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * n+1
distance = [INF]* n+1

for _ in range(m):
    node1, node2, cost = map(int,input().split())
    graph[node1].append([node2, cost])

#필요한 것 - 가장 짧은 노드 반환로직, 비용 비교로직, 최단거리 출력로직

def shortest_node():
    #미방문 노드중 가장 작은 cost를 가진 노드 반환
    min_value = INF
    index = 0
    for i in range(1,n+1):
        # 방문안했는데 min value보다 낮으면?
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #집중이 안된다. 내일 구현합시다
    pass
