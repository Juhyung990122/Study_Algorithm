from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 모든 코스요리의 조합을 구하고
    for i in course:
        com = []
        for j in orders:
            c = combinations(sorted(j),i)
            com += c
    # 몇명이 조합 주문했는지 체크
        count = Counter(com)
        print(count)
        if len(count) != 0 and max(count.values()) > 1:
            answer += [''.join(x) for x in count if count[x] == max(count.values())]
        return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))


