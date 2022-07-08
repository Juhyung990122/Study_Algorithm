import heapq

def solution(scoville, K):
    answer = 0
    heap = heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        answer += 1        
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))