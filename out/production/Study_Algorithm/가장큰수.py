def solution(numbers):
    answer = ""
    num = list(map(str,numbers))
    num.sort(key = lambda x : x*3, reverse=True)
    # 000처리를 위해서 int 로 변환 
    answer = str(int("".join(num)))
    return answer

print(solution([6, 10, 2]))