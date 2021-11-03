def solution(clothes):
    answer = 1
    closet = dict()

    for value,key in clothes:
        closet[key] = ["null"]

    for value,key in clothes:
        closet[key].append(value)
    
    for i in closet:
        answer *= len(closet[i])

    return answer-1
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))