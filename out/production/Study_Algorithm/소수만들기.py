def solution(nums):
    answer = 0
    from itertools import combinations
    num_list = combinations(nums,3)
    
    for n in num_list:
        prime = True
        sum = n[0] + n[1] + n[2]
        
        for i in range(2,sum):
            if sum % i == 0:
                prime = False
                break
        
        if prime == True:
            answer += 1
                
    return answer