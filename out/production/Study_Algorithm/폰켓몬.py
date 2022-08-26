def solution(nums):
    answer = 0
    nums_set = list(set(nums))
    
    if len(nums_set) < len(nums) // 2:
        answer = len(nums_set)
    else:
        answer = len(nums) // 2

    return answer

print(solution([3,3,3,2,2,2]))