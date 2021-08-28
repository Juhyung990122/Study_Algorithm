def solution(s):
    answer = ''
    #한글자씩 보면서
    now = 0
    while now < len(s):
        print(now, s[now],answer)
        if s[now].isdigit():
            answer += str(s[now])
            now += 1
            continue
        else:
            idx = now
            if s[idx] == 'z':
                answer += str(0)
                now += 4
                continue

            if s[idx] == 'o':
                answer += str(1)
                now += 3
                continue

            if s[idx] == 'e':
                answer += str(8)
                now += 5
                continue
            
            if s[idx] == 'n':
                answer += str(9)
                now += 4
                continue
            
            #t,f,s로 시작
            if s[idx+1] == 'w':
                answer += str(2)
                now += 3
                continue

            if s[idx+1] == 'h':
                answer += str(3)
                now += 5
                continue

            if s[idx+1] == 'o':
                answer += str(4)
                now += 4
                continue

            if s[idx+1] == 'i':
                if s[idx] == 'f':
                    answer += str(5)
                    now += 4
                    continue
                if s[idx] == 's':
                    answer += str(6)
                    now += 3
                    continue
            if s[idx+1] == 'e':
                answer += str(7)
                now += 5
                continue
    return answer

print(solution("123"))