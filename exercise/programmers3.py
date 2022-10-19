from itertools import permutations

def solution(k):
    answer = 0
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    heat = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    permutation_nums = list(permutations(num, 3)) + list(pernm)
    for i in range(10):
        permutation_nums.append((i,i,i))
        
    for nums in permutation_nums:
        if nums[0] == 0:
            hun = 0
        else:
            hun = heat[nums[0]]
        
        if nums[0] == 0 and nums[1] == 0:
            ten = 0
        else:
            ten = heat[nums[1]]

        if nums[2] == 0 and nums[1] == 0 and nums[0] == 0:
            one = 6
        else:
            one = heat[nums[2]]

        if hun + ten + one == k:
            print(nums)
            answer += 1

    return answer

print(solution(6))