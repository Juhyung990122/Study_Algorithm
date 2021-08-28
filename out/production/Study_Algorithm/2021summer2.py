
def solution(t, r):
    answer = []
    c_list = list()
    for i in range(len(t)):
        c_list.append([i,t[i],r[i]])
    c_list.sort(key = lambda x: x[0])
    c_list.sort(key = lambda x: x[1])
    while c_list:
        now = c_list.pop(0)
        answer.append(now[0])
        if c_list:
            if now[1] == c_list[0][1]:
                c_list[0][1] += 1
            c_list.sort(key = lambda x: x[0])
            c_list.sort(key = lambda x: x[1])

    return answer

print(solution([0,1,3,0],[0,1,2,3]))