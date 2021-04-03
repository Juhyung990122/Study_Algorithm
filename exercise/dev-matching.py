def solution(lottos, win_nums):
    answer = []
    min_correct = 0
    for i in range(6):
        if lottos[i] in win_nums:
            min_correct += 1
    
    max_correct = min_correct + lottos.count(0)

    for rank in [max_correct,min_correct]:
        if rank == 6:
            answer.append(1)
        elif rank == 5:
            answer.append(2)
        elif rank == 4:
            answer.append(3)
        elif rank == 3:
            answer.append(4)
        elif rank == 2:
            answer.append(5)
        else:
            answer.append(6)



    return answer
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))