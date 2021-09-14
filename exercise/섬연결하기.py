from collections import deque
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    road = set([costs[0][0]])
    while len(road) != n:
        for i,cost in enumerate(costs):
            if cost[0] in road and cost[1] in road:
                #시작점과 도착점이 둘다 이미 간 길에 있으면 사이클이므로 패스
                continue
            if cost[0] in road or cost[1] in road:
                #시작점이 있거나 도착점이 있거나 둘다 없으면 사이클 아니므로 길추가 + 비용갱신
                road.update([cost[0],cost[1]])
                answer += cost[2]
                #방문 표시
                costs[i] = [-1,-1,-1]
                break 
    return answer
print(solution(5,[[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]))
