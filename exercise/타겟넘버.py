from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque([[0,0]])
    while queue:
        num,idx = queue.popleft()
        if idx == len(numbers):
            if num == target:
                answer += 1
        else:
            add_num = numbers[idx]
            queue.append([num+add_num,idx+1])
            queue.append([num-add_num,idx+1])
            print(queue)
    return answer

print(solution([1, 2, 3, 4, 5],3))

