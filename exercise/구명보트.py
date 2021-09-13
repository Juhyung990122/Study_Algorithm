def solution(people, limit):
    answer = 0
    people = sorted(people)
    print(people)

    start = 0 
    end = len(people)
    while start < end:
        if len(people) == 1: 
            answer += 1
            break
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
    return answer

print(solution([70, 50, 80, 50],100))