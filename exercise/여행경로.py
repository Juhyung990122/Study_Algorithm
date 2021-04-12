from collections import deque
def solution(tickets):
    tickets.sort(reverse = True)
    road = dict()
    for start,end in tickets:
        if start in road:
            road[start].append(end)
        else:
            road[start] = [end]
        

    stack = ["ICN"]
    answer = []
    while stack:
        now = stack[-1]
        #출발지로 등록되어있지 않거나, 남은 티켓이 없거나
        if now not in road or len(road[now]) == 0:
            answer.append(stack.pop())
        #티켓하나 소비
        else:
            stack.append(road[now].pop())
    answer.reverse()
    return answer


print(solution([["ICN","A"],["A","B"],["B","A"],["A","ICN"],["ICN","A"]]))