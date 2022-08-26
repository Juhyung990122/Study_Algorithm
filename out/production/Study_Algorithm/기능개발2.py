from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    queue = []
    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while queue:
        if len(queue) == 1:
            answer.append(1)
            break

        target = queue.pop(0)
        count = 1
        while target >= queue[0]:
            queue.pop(0)
            count += 1

            if not queue:
                answer.append(count)
                return answer

        answer.append(count)
    return answer

print(solution([93,30,55], [1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([99, 1, 99, 1], [1, 1, 1, 1]))
print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]))
