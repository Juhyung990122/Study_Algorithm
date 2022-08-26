def solution(a, b):
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    d = 0
    for i in range(0,a):
        d += months[i]
    d += b
    return week[d % 7 - 1]
print(solution(5,24))