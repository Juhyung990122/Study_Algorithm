def convert_time(time):
    time = time.split(":")
    h = int(time[0])
    m = int(time[1])
    return (h * 60) + m

def convert_str(sum_m):
    h = str(sum_m // 60)
    m = str(sum_m % 60)
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    return h + ":" + m

def solution(log):
    answer = ''
    sum_min = 0 
    for i in range(0,len(log),2):
        start = convert_time(log[i])
        end = convert_time(log[i+1])

        if end - start < 5 : 
            continue

        if end - start >= 105:
            sum_min += 105
            continue

        sum_min += end - start

    answer = convert_str(sum_min)
    return answer

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))