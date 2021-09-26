from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for j in orders:
            c = combinations(sorted(j),i)
            temp+=c
        counter = Counter(temp)
        print(counter)
        # 원소가 없지 않거나, 맥스값이 1이상일때 (2명 이상 시킨 메뉴들로만 구성되어야하기때문)
        if len(counter) != 0 and max(counter.values())>1:
            # 맥스값을 가진 카운터들만 답에 넣기
            answer += [''.join(x) for x in counter if counter[x] == max(counter.values())]
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))


