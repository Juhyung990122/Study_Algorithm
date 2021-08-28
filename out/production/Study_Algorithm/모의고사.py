def solution(answers):
    answer = []
    solve_num = [0] * 3
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    num1 = list()
    num2 = list()
    num3 = list()
    for i in range(len(answers)):
        num1.append(pattern1[i % len(pattern1)])
        num2.append(pattern2[i % len(pattern2)])
        num3.append(pattern3[i % len(pattern3)])
     
    for i in range(len(answers)):
        if answers[i] == num1[i]:
            solve_num[0] += 1
        if answers[i] == num2[i]:
            solve_num[1] += 1
        if answers[i] == num3[i]:
            solve_num[2] += 1
            
    max_num = max(solve_num)
    for i in range(len(solve_num)):
        if max_num == solve_num[i]:
            answer.append(i+1)
        answer.sort()
        
    return answer