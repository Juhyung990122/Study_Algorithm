def solution(arr):
    answer = [0,0,0]
    num = {1 : 0, 2 : 0, 3 : 0}
    for i in arr:
        num[i] += 1
    m = max(num.values())
    for k in num.keys():
        answer[k-1] = m - num[k]
    return answer

print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))
print(solution([1,2,3]))
