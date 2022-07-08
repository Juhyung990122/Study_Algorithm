def solution(arr):
    answer = [0,0,0]
    num = {1 : 0, 2 : 0, 3 : 0}
    for i in arr:
        num[i] += 1
    m = max(num.values())
    for k in num.keys():
        answer[k-1] = m - num[k]
    return answer