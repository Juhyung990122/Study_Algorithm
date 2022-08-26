def solution(time, plans):
    answer = ''
    for c,s,e in plans:
        holiday = 0
        s_type = s[-2:]
        s_time = int(s[:-2])
        if s_type == "PM":
            s_time += 12

        e_type = e[-2:]
        e_time = int(e[:-2])
        if e_type == "PM":
            e_time += 12

        if s_time <= 9.5:
            holiday += 8.5
        elif 9.5 < s_time <= 18:
            holiday += 18 - s_time
        else:
            holiday += 0

        if e_time <= 13:
            holiday += 0
        elif 13 < e_time <= 18:
            holiday += e_time - 13
        else:
            holiday += 5

        if holiday <= time:
            time -= holiday
            answer = c
        else:
            break
    return answer
print(solution(3.5	,[ ["홍콩", "11PM", "9AM"], ["엘에이", "5PM", "2PM"] ]))