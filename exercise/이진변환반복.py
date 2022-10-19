def solution(s):
    answer = [0,0]
    while s != "1":
        answer[0] += 1
        parse_s = str(s).replace("0", "")
        answer[1] += len(s) - len(parse_s)
        s = format(len(parse_s),'b')
        
    return answer

print(solution("110010101001"))