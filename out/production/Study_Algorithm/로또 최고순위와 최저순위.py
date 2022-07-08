def solution(lottos, win_nums):
    answer = []
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    count = 0
    for i in lottos:
        if i in win_nums:
            count+= 1
    lowest = rank[count]
    highest = rank[lottos.count(0) + count]
    return [highest,lowest]
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))