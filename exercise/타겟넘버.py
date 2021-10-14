def solution(numbers, target):
    answer = 0
    queue = list([[0,0]])
    while queue:
        num,idx = queue.pop(0)
        if idx == len(numbers):
            if num == target:
                answer += 1
        else:
            add_num = numbers[idx]
            queue.append([num+add_num,idx+1])
            queue.append([num-add_num,idx+1])

    return answer

print(solution([1, 2, 3, 4, 5],3))