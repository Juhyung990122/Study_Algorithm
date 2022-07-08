def solution(s):
    answer = []
    s = list(s)
    index = [-1 for _ in range(len(s))]
    
    i = 0
    now = 0
    while True:
        while True:
            index[i%len(s)] = now
            if s[i % len(s)] == s[(i+1) % len(s)]:
                i += 1
            else:
                now = i + 1
                i += 1
                break
        if i >= len(s):
            break
    
    s_index = list(set(index))
    for i in s_index:
        answer.append(index.count(i))
    
    return sorted(answer)
print(solution("aaabbaaa"))