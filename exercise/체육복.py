def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()

    for i in lost:
        if i in reserve:
            reserve.pop()
            lost.pop()
            

    # for i in reserve:
    #     if i-1 in lost:
    #         lost.remove(i-1)
    #         continue
    #     if i+1 in lost:
    #         lost.remove(i+1)
    #         continue
    return answer - len(lost)

print(solution( 2, [2, 1], [1, 2]))

