import itertools

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    pick = []
    for i in range(1, len(num_list)+1):
        pick.append((itertools.permutations(num_list,i)))
    
    per_list = []
    for i in pick:
        for j in i:
            per_list.append(int("".join(j)))
    
    per_list = list(set(per_list))

    for i in per_list:
        num = i
        if num == 2 or num == 3:
            answer += 1
            continue
        if num < 2:
            continue

        flag = True
        for j in range(2, num):
            if num % j == 0:
                flag = False
                break

        if flag:        
            answer += 1
    return answer

print(solution("011"))